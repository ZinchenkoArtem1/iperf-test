import pytest
import parser


class TestSuite:

    @pytest.mark.usefixtures("server")
    def test_iperf3_client_connection(self, client):
        if client.returncode == 0:
            for value in parser.parser(client):
                print(value)
                assert value["Transfer"] > 2 and value["Bandwidth"] > 20
        else:
            raise Exception(parser.parse_error(client))

