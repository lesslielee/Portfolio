import http.server
import socketserver
import cgi
import urllib.parse
import uuid
import json


class UploadHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(message.encode())

    def do_POST(self):
        content_type, _ = cgi.parse_header(self.headers['content-type'])
        video_id = "7788f75d-2c37-4ab3-a3ce-b84472534734"
        uploaded_file = None
        actual_number_value = None
        session_id = None
        is_correct = None

        if content_type == 'multipart/form-data':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
            if 'video' in form:
                uploaded_file = form['video']
            if 'actual_number' in form:
                actual_number_value = form.getfirst('actual_number')
            if 'video_id' in form:
                session_id = form.getfirst('video_id')
            if 'is_correct' in form:
                is_correct = form.getfirst('is_correct')

            # For Upload file to server
            if uploaded_file is not None and actual_number_value is not None:
                with open(uploaded_file.filename, 'wb') as f:
                    f.write(uploaded_file.file.read())

                ## JSON response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                response_data = {
                    'message': 'File uploaded successfully.',
                    # 'filename': uploaded_file.filename,

                    'video_id': '7788f75d-2c37-4ab3-a3ce-b84472534734',
                    'actual_number': 5, #actual_number_value,
                }

                response_content = json.dumps(response_data)
                self.wfile.write(response_content.encode('utf-8'))


                print("Received actual_number: %s" % actual_number_value)
                print("Received video_file: %s" % uploaded_file.filename)
                print("Generated video_id: %s" % video_id)


            elif session_id is not None and is_correct is not None:
                ## JSON response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                response_data = {
                    'message': 'User feedback successfully.',
                    # 'video_id': video_id,
                    # 'is_correct': is_correct,
                }

                response_content = json.dumps(response_data)
                self.wfile.write(response_content.encode('utf-8'))


                print("Received video_id: %s" % video_id)
                print("Received user feedback: %s" % is_correct)
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'No file was uploaded.')
        elif content_type == 'text/plain':
            content_length = int(self.headers['content-length'])
            post_data = self.rfile.read(content_length).decode('utf-8')

            print("Received text/plain POST data:")
            print(post_data)

            response_message = "Text data received and processed."
            self._send_response(response_message)
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid content type.')

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        if 'video_id' in query_params:
            id_value = '7788f75d-2c37-4ab3-a3ce-b84472534734' #query_params['video_id'][0]
            predicted_number = 6
            response_data = {
                'message': 'AI Guess result is ready',
                'video_id': '7788f75d-2c37-4ab3-a3ce-b84472534734',
                'predicted_number': 6, #  predicted_number,
            }


            if id_value == '7788f75d-2c37-4ab3-a3ce-b84472534734':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                # self.wfile.write(b'Query result for ID 1234')
                response_content = json.dumps(response_data)
                self.wfile.write(response_content.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'ID not found')
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Missing ID parameter')


if __name__ == "__main__":
    PORT = 8000

    with socketserver.TCPServer(("", PORT), UploadHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
