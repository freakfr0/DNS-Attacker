
# DNS Query

This is a simple DNS query tool that allows you to query a DNS server for a specific domain and retrieve the corresponding IP address.

## Usage

To use this tool, you need to have Python 3 installed on your system. You can then run the tool from the command line as follows:

```
python dns_query.py <domain> [--dns-server <dns_server>]
```

Where `<domain>` is the domain you want to query, and `<dns_server>` is the DNS server you want to query. If you don't specify a DNS server, the tool will use the default DNS server (8.8.8.8).

## Example

To query the IP address of google.com, you can run the following command:

```
python dns_query.py google.com
```

This will output the IP address of google.com, along with the TTL and DNS server used to query the domain.

## License

This tool is licensed under the MIT License. See the LICENSE file for more information.
```
