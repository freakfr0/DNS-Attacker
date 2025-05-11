import socket
import struct
import random
import argparse
import dns.resolver
import dns.exception
import dns.rdatatype
import dns.rdataclass
import dns.message
import dns.query
import dns.flags
import dns.name
import dns.rdata
import dns.rdtypes

def dns_query(domain, dns_server):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)

    # Create a DNS query packet
    query = struct.pack('!H', random.randint(0, 65535))  # Transaction ID
    query += struct.pack('!H', 0x0100)  # Flags
    query += struct.pack('!H', 1)  # Questions
    query += struct.pack('!H', 0)  # Answer RRs
    query += struct.pack('!H', 0)  # Authority RRs
    query += struct.pack('!H', 0)  # Additional RRs

    # Add the domain name to the query
    for part in domain.split('.'):
        query += struct.pack('!B', len(part))
        query += part.encode()
    query += struct.pack('!B', 0)  # Null terminator

    # Add the query type and class
    query += struct.pack('!H', 1)  # Type A
    query += struct.pack('!H', 1)  # Class IN

    # Send the query to the DNS server
    sock.sendto(query, (dns_server, 53))

    # Receive the response
    response, _ = sock.recvfrom(512)

    # Parse the response
    response = response[12:]  # Skip the header
    response = response[4:]  # Skip the question section

    # Check if the response is truncated
    if response[2] & 0x02:
        print("Response is truncated")
        return

    # Check if the response has an answer
    if response[2] & 0x01:
        print("No answer in the response")
        return

    # Parse the answer section
    answer = response[12:]  # Skip the header and question section
    answer = answer[4:]  # Skip the name
    answer = answer[4:]  # Skip the type and class
    ttl = struct.unpack('!I', answer[:4])[0]
    data_length = struct.unpack('!H', answer[4:6])[0]
    ip_address = socket.inet_ntoa(answer[6:10])

    print(f"Domain: {domain}")
    print(f"DNS Server: {dns_server}")
    print(f"TTL: {ttl}")
    print(f"IP Address: {ip_address}")

def main():
    parser = argparse.ArgumentParser(description='DNS Query Tool')
    parser.add_argument('domain', help='The domain to query')
    parser.add_argument('--dns-server', default='8.8.8.8', help='The DNS server to query')
    args = parser.parse_args()

    dns_query(args.domain, args.dns_server)

if __name__ == '__main__':
    main()
