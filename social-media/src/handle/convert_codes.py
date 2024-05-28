import grpc


def convert_grpc_code_into_http(err: grpc.RpcError):
    http_code = 500
    if err.code() == grpc.StatusCode.PERMISSION_DENIED:
        http_code = 403
    elif err.code() == grpc.StatusCode.NOT_FOUND:
        http_code = 404
    return http_code

