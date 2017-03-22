# Am I OK

How do you do? Am I OK checks a website's HTTP status code to see if they are well. A status code 200 returns "OK". Otherwise, it returns "Not OK"

## Getting Started

Download or clone git repository.

1. Import Am I OK:

        $ python
        >>> from amiok.app import get_status

2. Ask if a website is OK:

        >>> get_status("http://google.com")
        'OK'

        >>> get_status("http://not-the-google.com")
        'Not OK'

## Code Status

[![Build Status](https://travis-ci.org/Cloudplement/amiok.svg?branch=master)](https://travis-ci.org/Cloudplement/amiok) [![Code Climate](https://codeclimate.com/github/Cloudplement/amiok/badges/gpa.svg)](https://codeclimate.com/github/Cloudplement/amiok)

## License

Am I OK is released under the [MIT License](http://www.opensource.org/licenses/MIT).
