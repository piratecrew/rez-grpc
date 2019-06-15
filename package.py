name = "grpc"

version = "1.21.3"

authors = [
    "Google"
]

description = \
    """
    gRPC is a modern open source high performance RPC framework that can run in any environment. 
    It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. 
    It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.
    """

@early()
def variants():
    from rez.package_py_utils import expand_requires
    requires = ["platform-**"]
    return [expand_requires(*requires)]

tools = [
    "protoc",
]

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    if building:
        env.CMAKE_MODULE_PATH.prepend("{root}/cmake")
