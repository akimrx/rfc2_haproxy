
def test_nginx(host):
    """Checking the installation and operation of the NTP service."""
    haproxy = host.package("haproxy")
    haproxy_service = host.service("haproxy")
    assert haproxy.is_installed, "HAProxy is not installed"
    assert haproxy_service.is_running, "HAProxy service is not running"
    assert haproxy_service.is_enabled, "HAProxy service is not enabled"
