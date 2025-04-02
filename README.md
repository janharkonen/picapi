# PicAPI

A simple API for uploading and manipulating images directly from URL parameters.

## Overview

PicAPI provides a straightforward way to upload images and apply transformations using URL parameters. This makes it easy to integrate image processing into your applications without complex client-side code.

## Features

- Simple image upload
- Get URL for your pictures
- Sprinkle in custom commands in picture URL to get an edited picture

## Tech Stack

- **Frontend**: Raw HTML and Vanilla JS
- **API**: Flask
- **Database**: SQLite
- **Deployment**: Whatever you like! (I use Hetzner VPS)
- **Picture storage**: Local file system (Also in my Hetzner VPS)

## Getting Started

#### Using Docker

1. Install docker and then run
   ```bash
   ./runapi.sh
   ```
### How I configured Nginx

```nginx
server {
    listen 80;
    listen 443 ssl;
    server_name picapi.janharkonen.fi;

    ssl_certificate /etc/letsencrypt/live/picapi.janharkonen.fi/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/picapi.janharkonen.fi/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;

    # Access and error logs for debugging
    access_log /var/log/nginx/picapi.janharkonen.fi.access.log;
    error_log /var/log/nginx/picapi.janharkonen.fi.error.log;

    # Frontend app - direct file serving
    location / {
        root /home/jan/picapi/Frontend;
        index picapi.html;
        # Simplified try_files to prevent redirect loops
        try_files $uri $uri/ =404;
    }

    # Handle the favicon.ico request specifically
    location = /favicon.ico {
        return 204; # Return No Content status to prevent errors
        access_log off;
        log_not_found off;
    }
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
