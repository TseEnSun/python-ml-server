# python-ml-server

## How to run the server?

```
docker compose build
docker compose up
```

There is a pre-start that will create the first user by the name and password in the .env file.
During the pre-start, the DB migration will also trigger, then the User, Search, and Feedback tables will be created.
After `docker compose up`, the server should run at 0.0.0.0 and 80 ports. 
http://0.0.0.0/sticker-search/docs will let you access the Swagger UI.


P.S. I found that the ImageSearch class consumes a large size of memory (15G~). 
But I still need to run it on my machine. Thus, I created a dummy search without any model, just an offset of the hash of the input text.

## TODO

* Unit Test
  * API Endpoint
    * feedback
    * report
    * search
    * user
    * login
  * db
    * crud
      * feedback
      * search
      * user
  * services
    * image_search

* Deep dive into ImageSearch which cost too much mempry
  * Memory increasing when generating image_vectors (15G~)
    * Use no_grad() to save memory

* Refind the search result encode method storing in DB.
  