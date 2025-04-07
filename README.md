# PicAPI

A simple API for uploading and manipulating images directly from URL parameters.

## Overview

PicAPI provides a straightforward way to upload images and apply transformations using URL parameters. This makes it easy to integrate image processing into your applications without complex client-side code.

## Features

- Simple image upload
- Get URL for your pictures
- Sprinkle in custom commands in picture URL to get an edited picture

## How to use the API ?!?!?!@??!?!?!?!?!?

The following URL are live and fully functional, so feel free to try them yourself!

Say you have a picture saved in your server from your domain
```
https://picapi.janharkonen.fi/api/pics/012f04b4f4bf4219a5ab1ae67b97eb7e.jpg
```
This will return you the picture that you saved as is.

But it isn't quite right for whatever reason.
I want to add 15% padding on all sides. Then I add the `BG=115` to the URL as a parameter.
```
https://picapi.janharkonen.fi/api/pics/012f04b4f4bf4219a5ab1ae67b97eb7e.jpg?BG=115
```
But I want to add more width than height. Say twice the width, but only 25% of the height. Then I can user the width and height background parameters `BGw=200` and `BGh=125`.
```
https://picapi.janharkonen.fi/api/pics/012f04b4f4bf4219a5ab1ae67b97eb7e.jpg?BGw=200&BGh=125
```
Say the default background color is awful. You can change the background color e.g. as white with the `BGc=white` parameter. The API currently supports white and black background colors, otherwise it defaults to grey.
```
https://picapi.janharkonen.fi/api/pics/012f04b4f4bf4219a5ab1ae67b97eb7e.jpg?BGc=white&BGw=200&BGh=125
```
IMPORTANT! The background color should be applied first in the url. Just because.

You can also crop the images. This was implemented by pure accident, by it could be useful. Just user the `BG`, `BGw` and `BGh` parameters with values with less than 100%.
```
https://picapi.janharkonen.fi/api/pics/012f04b4f4bf4219a5ab1ae67b97eb7e.jpg?BGw=90&BGh=20
```
You can extend/crop images also in one of the cardinal directions: left, right, top, bottom with the commands `BGl`, `BGr`, `BGt` and `BGb`respectively.
## Improvements in the future
Here are some suggestions to improve the code. Feel free to submit a PR!
- Ability to arbitrarily choose background color
- Make ImageTransformer class more of a functional programming style (maybe extend PIL.Image class or include PIL.Image instace as an attribute?)
- Make ImageBucket to fetch images from S3 instead of the Hetzner Cloud VPS's local storage.
- Regular database audit (Check that the rows in the SQLite metadata correspond to pictures actually saved in the server)
- Better UI
- Automatic backups somehow
- Dev and prod environment improvement (now you have to manually comment out the API URLs based on if you're in prod or dev)
- SVG manipulating support
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

### SQLite
This is a cheat sheet for myself.
 - To run SQLite database, use
```bash
sqlite3 PicMetadata.db
```
 - Within the CLI you see all tables with
```bash
.tables
```
 - And to see content of a table just write
```bash
SELECT * FROM PIC_METADATA
```
 - The output is ugly so input
```bash
.headers on
.mode column
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.