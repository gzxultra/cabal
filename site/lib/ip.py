# coding: utf-8


class NoRemoteAddrException():
    pass


def get_ip_by_request(request):
    ips = ''
    if "HTTP_X_FORWARDED_FOR" in request.environ:
        ips = request.environ["HTTP_X_FORWARDED_FOR"]

    if not ips and 'HTTP_X_REAL_IP' in request.environ:
        ips = request.environ["HTTP_X_REAL_IP"]

    if not ips:
        ips = request.environ.get("REMOTE_ADDR")

    if not ips:
        raise NoRemoteAddrException()

    return ips.split(',')[0].strip()
