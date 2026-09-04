#!/bin/bash

read -p "Nhập URL (ví dụ: http://site/page.php?id=): " url

for i in {0..99}
do
    echo "===== Request: $i ====="

    response=$(curl -s -w "\nHTTP_STATUS:%{http_code}" "${url}${i}")

    status=$(echo "$response" | grep "HTTP_STATUS" | cut -d: -f2)

    body=$(echo "$response" | sed '/HTTP_STATUS/d')

    echo "Status code: $status"
    echo "Reponse length: ${#body}"

    echo
done
