from core import FM
import traceback


class ReadFile(FM.BaseAction):
    def __init__(self, request, path, encoding, session, **kwargs):
        super(ReadFile, self).__init__(request=request, **kwargs)

        self.path = path
        self.session = session
        self.encoding = encoding

    def run(self):
        request = self.get_rpc_request()

        result = request.request_bytes('sftp/read_file', login=self.request.get_current_user(),
                                       password=self.request.get_current_password(), path=self.path,
                                       session=self.session, encoding=self.encoding)
        answer = self.process_result(result)

        if 'data' in answer.keys():
            data = answer['data']
            if 'content' in data.keys() and 'encoding' in data.keys():
                data['encoding'] = data['encoding'].decode('utf-8').lower()
                data['content'] = str(data['content'], data['encoding'], 'replace')
                data['item'] = self.byte_to_unicode_dict(data['item'])
                answer['data'] = data
        if 'error' in answer.keys():
            # FIXME
            answer["error"] = answer['error'] if answer['error'] is not None else True

        if 'message' in answer.keys():
            try:
                message = answer['message'].decode('utf-8') if answer['message'] is not None else ''
                answer['message'] = message
            except Exception as e:
                self.application.logger.error(
                    "Handled exception in action ReadFile: " + str(e) + "Traceback:" + traceback.format_exc())

        if 'traceback' in answer.keys():
            try:
                trace = answer['traceback'].decode('utf-8') if answer['traceback'] is not None else ''
                answer['traceback'] = trace
            except Exception as e:
                self.application.logger.error(
                    "Handled exception in action ReadFile: " + str(e) + "Traceback:" + traceback.format_exc())

        return answer

    def byte_to_unicode_dict(self, answer):
        decoded = {}
        for key in answer:
            if isinstance(key, bytes):
                unicode_key = key.decode("utf-8")
            else:
                unicode_key = key

            if isinstance(answer[key], dict):
                decoded[unicode_key] = self.byte_to_unicode_dict(answer[key])
            elif isinstance(answer[key], list):
                decoded[unicode_key] = self.byte_to_unicode_list(answer[key])
            elif isinstance(answer[key], int):
                decoded[unicode_key] = answer[key]
            elif isinstance(answer[key], float):
                decoded[unicode_key] = answer[key]
            elif isinstance(answer[key], str):
                decoded[unicode_key] = answer[key]
            elif answer[key] is None:
                decoded[unicode_key] = answer[key]
            else:
                try:
                    decoded[unicode_key] = answer[key].decode("utf-8")
                except UnicodeDecodeError:
                    # Костыль для кракозябр
                    decoded[unicode_key] = answer[key].decode("ISO-8859-1")
        return decoded

    def byte_to_unicode_list(self, answer):
        decoded = []
        for item in answer:
            if isinstance(item, dict):
                decoded_item = self.byte_to_unicode_dict(item)
                decoded.append(decoded_item)
            elif isinstance(item, list):
                decoded_item = self.byte_to_unicode_list(item)
                decoded.append(decoded_item)
            elif isinstance(item, int):
                decoded.append(item)
            elif isinstance(item, float):
                decoded.append(item)
            elif item is None:
                decoded.append(item)
            else:
                try:
                    decoded_item = item.decode("utf-8")
                except UnicodeDecodeError:
                    # Костыль для кракозябр
                    decoded_item = item.decode("ISO-8859-1")
                decoded.append(decoded_item)
        return decoded
