class Login extends BB.View

  el: '#login-container'

  events:
    'submit #login-form': 'loginSubmit'

  initialize: () ->
    @login_form = $('#login-form', @$el)
    @login_button = $('#login-submit')

  loginSubmit: (e) ->
    e.preventDefault();
    if @login_button.hasClass('disabled')
      return

    @login_button.button('loading')
    form_data = BB.Form.toObject(@login_form);
    BB.Transport.ajaxRequest '/auth',
      data: form_data
      success: (data) =>
        if !data.error
          window.location = data.url

      error: (response) =>
        data = response.responseJSON || {}
        if data.error
          BB.Form.renderErrorOutput(@login_form, data.message, data.errors)
        @login_button.button('reset')
        @render()