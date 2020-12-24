# Media project with tree-like comments

This is a backend of a media project with nested comments implementation.

### Base URL

```
api/v1
```

### What does it consist of

[Posts](#posts)

[Comments](#comments)

[Users](#users)

## Posts

#### Posts list

```
GET /posts
```

Return a list of posts sorted by novelty and rating.

```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "author": 3,
            "published": "2020-12-23T14:45:28.570599Z",
            "updated": "2020-12-24T02:47:59.497122Z",
            "title": "How slowly the time passes here",
            "content": "Yet a second step is taken towards my enterprise. I have hired a vessel and am occupied in collecting my sailors; those whom I have already engaged appear to be men on whom I can depend and are certainly possessed of dauntless courage.",
            "rating": 6127497,
            "views": 10573614,
            "comments_number": 0
        },
        {
            "id": 2,
            "author": 2,
            "published": "2020-12-23T13:51:34.294329Z",
            "updated": "2020-12-23T14:56:45.583316Z",
            "title": "The Red-Headed League",
            "content": "The portly client puffed out his chest with an appearance of some little pride, and pulled a dirty and wrinkled newspaper from the inside pocket of his great-coat. As he glanced down the advertisement column, with his head thrust forward, and the paper flattened out upon his knee, I took a good look at the man, and endeavored, after the fashion of my companion, to read the indications which might be presented by his dress or appearance.",
            "rating": 2477469,
            "views": 7432407,
            "comments_number": 0
        },
        {
            "id": 1,
            "author": 2,
            "published": "2020-12-22T19:32:46.390182Z",
            "updated": "2020-12-24T02:48:21.265697Z",
            "title": "A Scandal In Bohemia",
            "content": "I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise, but admirably balanced mind.",
            "rating": 2850795,
            "views": 8552387,
            "comments_number": 6
        }
    ]
}
```

#### Post detail

```
/posts/{id}
```

Allowed methods:
```GET```
```POST```
```PUT```
```PATCH```
```DELETE```*

*For 4 last methods an authentication token must be provided in the "Authorization" HTTP header (for any resource).

## Comments

#### Comments list

```
GET /posts/{id}/comments
```

Return a list of comments to a specific post.

```
GET /posts/1/comments
```

```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 5,
            "author": 3,
            "parent": null,
            "content": "What should he do now?",
            "published": "2020-12-23T14:48:28.691878Z",
            "updated": "2020-12-23T14:55:01.341174Z",
            "rating": 4,
            "children": []
        },
        {
            "id": 1,
            "author": 2,
            "parent": null,
            "content": "His boss would certainly come round with the doctor.",
            "published": "2020-12-22T19:33:34.996628Z",
            "updated": "2020-12-23T14:54:13.356175Z",
            "rating": 5,
            "children": [
                {
                    "id": 2,
                    "author": 3,
                    "parent": 1,
                    "content": "But that would be extremely strained and suspicious as in fifteen years of service Gregor had never once yet been ill.",
                    "published": "2020-12-22T19:34:05.985817Z",
                    "updated": "2020-12-23T14:54:31.062237Z",
                    "rating": 4,
                    "children": [
                        {
                            "id": 4,
                            "author": 2,
                            "parent": 2,
                            "content": "The office assistant was the boss's man, spineless, and with no understanding",
                            "published": "2020-12-23T14:47:47.556979Z",
                            "updated": "2020-12-23T14:54:51.705420Z",
                            "rating": 3,
                            "children": []
                        },
                        {
                            "id": 3,
                            "author": 3,
                            "parent": 2,
                            "content": "What about if he reported sick?",
                            "published": "2020-12-23T08:09:00.144535Z",
                            "updated": "2020-12-23T14:54:42.216050Z",
                            "rating": 8,
                            "children": [
                                {
                                    "id": 6,
                                    "author": 2,
                                    "parent": 3,
                                    "content": "Had the alarm clock not rung?",
                                    "published": "2020-12-23T14:49:34.971841Z",
                                    "updated": "2020-12-23T14:55:12.624804Z",
                                    "rating": 1,
                                    "children": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```

#### Comment detail

```
/posts/{id}/comments/{id}
```
Allowed methods:
```GET```
```POST```
```PUT```
```PATCH```
```DELETE```

## Users
#### Users list
```
GET /users
```

Return a list of users.

#### User detail

```
/users/{id}
```

Allowed methods:
```GET```
```POST```
```PUT```
```PATCH```
```DELETE```


#### User's posts list

```
GET /users/{id}/posts
```

Return a list of posts published by a specific user.

```
GET /users/3/posts
```

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "author": 3,
            "published": "2020-12-23T14:45:28.570599Z",
            "updated": "2020-12-24T02:47:59.497122Z",
            "title": "How slowly the time passes here",
            "content": "Yet a second step is taken towards my enterprise. I have hired a vessel and am occupied in collecting my sailors; those whom I have already engaged appear to be men on whom I can depend and are certainly possessed of dauntless courage.",
            "rating": 6127497,
            "views": 10573614,
            "comments_number": 0
        }
    ]
}
```
