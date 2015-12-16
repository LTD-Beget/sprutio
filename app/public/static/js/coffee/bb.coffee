# Extends jquery
$.fn.serializeObject =  () ->
  "use strict";
  result = {};
  extend = (i, element) ->
    node = result[element.name];
    #If node with same name exists already, need to convert it to an array as it
    #is a multi-value field (i.e., checkboxes)
    if 'undefined' != typeof node && node != null
      if $.isArray(node)
        node.push(element.value)
      else
        result[element.name] = [node, element.value]
    else
      result[element.name] = element.value

  $.each(this.serializeArray(), extend);
  return result

# Namespace
BB = ()->

# Base app widget
class BB.Widget extends Backbone.View

  render: () ->
    @delegateEvents()
    return @

  initialize: () ->
    #initialize view

# Base app view
class BB.View extends BB.Widget

  initialize: () ->
    #initialize view

# Base app events
BB.Events = _.extend({}, Backbone.Events);
BB.Events.KEY_ENTER = 13;
BB.Events.KEY_S = 83;
BB.Events.KEY_MAC_CMD_S = 19;
BB.Events.KEY_CTRL_S = (e) ->
  return !(!(e.which == BB.Events.KEY_S && e.ctrlKey) && !(e.which == BB.Events.KEY_MAC_CMD_S))

# Base app model
class BB.Model extends Backbone.Model

  methodToURL = {}

  sync: (method, model, options) ->

    options = options || {};
    method = method.toLowerCase();

    options.type = 'POST';

    if method == 'create'
      options.url = model.methodToURL[method]
    else
      options.url = model.methodToURL[method] + model.get('id')

    return Backbone.sync.apply(@, arguments)

  parse: (response) ->
    return response.data || {}

  initialize: () ->
    #initialize model

# mobile helpers namespace
class BB.Device
  constructor: () ->
  @isMobile: () ->
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)

# Data helper
class BB.Data
  constructor: () ->
  @Extend: () ->
    args = [true, {}]
    for argument in arguments
      args.push(argument)

    return $.extend.apply(this, args)

class BB.Transport
  constructor: () ->

  @ajaxRequest: (url, options) ->
    defaults = {
      dataType:'json',
      type:'POST',
      error:() ->
        #console.log('ajax error here')
    }

    options = _.extend(defaults, options || {})
    return $.ajax(url, options)

  @submitData: (url, options) ->
    defaults = {
      data: {}
      method: 'POST'
      target: '_self'
    }

    options = _.extend(defaults, options || {})

    form = $('#_hidden_form')
    if form.length > 0
      form.remove()

    form = $('<form id="_hidden_form"></form>')
    .attr('action', url)
    .attr('method', options.method)
    .attr('target', options.target)
    .appendTo($('body'))

    for item of options.data
      if options.data.hasOwnProperty(item)
        #console.log(item, options.data[item]);
        $('<input>')
        .attr('name', item)
        .val(options.data[item])
        .appendTo(form)

    form.submit()

# Form helper
class BB.Form
  constructor: () ->
  @renderErrorOutput: (container, message, errors) ->
    output = $('.output div.alert', container).html('');
    $('<h5></h5>').text(message).appendTo(output);

    if errors? and errors.length > 0
      errors_list = $('<ul></ul>')

      for error in errors
        $('<li></li>').text(error).appendTo(errors_list)

      errors_list.appendTo(output)
      $('.output', container).slideDown(100)

  @hideErrorOutput: (container) ->
    $('.output', container).slideUp(100)
    $('.output div.alert', container).html('')

  @beforeSubmit: (container) ->
    elements = $('[data-before-submit]', container);
    elements.filter('.button, .btn').each () ->
      width = $(@).outerWidth();
      $(@).css({'width': width + 'px'}).button('loading')

  @reloadCaptcha: (container) ->
    image = if ($(container).tagName == 'img') then $(container) else $('img', $(container))[0]
    $image = $(image);
    new_src = $image.url().attr('path') + '/?' + Math.random();
    $image.attr("src", new_src)

  @resetForm: (container) ->
    elements = $('form', container);
    elements.each () ->
      $(@)[0].reset()

    try
      $('select.selectpicker', container).selectpicker('render')
    catch
      return

  @afterSubmit: (container) ->
    elements = $('[data-before-submit]', container);
    elements.filter('.btn, .button').each () ->
      $(@).button('reset')

  @toObject: (element, extra_data) ->
    extra_data = extra_data || {};
    fields = $('input[type=hidden], input[type=text], input[type=password], input[type=email], input[type=checkbox]:checked, input[type=radio]:checked, select, textarea', $(element)).not(':disabled');
    fields_data = $(fields).serializeObject()
    return _.extend(extra_data, fields_data)