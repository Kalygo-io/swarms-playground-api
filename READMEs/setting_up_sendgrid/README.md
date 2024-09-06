# TLDR

Documenting process of setting up SendGrid

## Log

- signed up on https://sendgrid.com/en-us
- Followed `Integration Guide`
  - https://app.sendgrid.com/guide/integrate
  - using WebAPI approach (Python)
  - pip install sendgrid (v6.11.0)
  - add ENV var called SENDGRID_API_KEY
  - create background job called `send_password_reset_email`
  - 

## Links

- https://app.sendgrid.com/guide/integrate/langs/python