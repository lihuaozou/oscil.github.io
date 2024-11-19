import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print("在浏览器中打开上面的链接来查看网站")
    print("按 Ctrl+C 可以停止服务器")
    httpd.serve_forever()
