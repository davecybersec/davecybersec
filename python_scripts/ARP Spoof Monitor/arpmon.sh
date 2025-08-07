#!/bin/bash

# Check if the user has provided an IP address
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <IP_ADDRESS>"
    exit 1
fi

IP_ADDRESS=$1

# Get the MAC address for the given IP
get_mac_address() {
    arp -an | grep -w "$IP_ADDRESS" | awk '{print $4}'
}

# Display initial MAC address
INITIAL_MAC=$(get_mac_address)

if [ -z "$INITIAL_MAC" ]; then
    echo "No MAC address found for IP: $IP_ADDRESS. Ensure the IP is reachable."
    exit 1
fi

echo "Monitoring MAC address for IP: $IP_ADDRESS"
echo "Initial MAC address: $INITIAL_MAC"

# Monitor the ARP table and display any changes
while true; do
    CURRENT_MAC=$(get_mac_address)
    if [ "$CURRENT_MAC" != "$INITIAL_MAC" ]; then
        echo "MAC address change detected for IP: $IP_ADDRESS"
        echo "Previous MAC: $INITIAL_MAC"
        echo "Current MAC: $CURRENT_MAC"
        exit 1
    fi
    sleep 5
done
