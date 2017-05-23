##Docker Registries

So we've been using a lot of Docker images without really talking about where they come from. Docker images are retrieved from registries and published through registries. Registries are pieces of software and there are several options that you can choose if you want to run a registry.

They're pieces of software that manage and distribute images. You upload images to them. You can download images from them and they let you search to find the images you want to use. Docker, the company, makes these freely available.

You can also run your own as well. Many companies choose to run their own registry within their company to ensure that their data stays safe and private.



```
Docker Registries

- Registries manage and distribute images
- Docker (the company) offers these for free
- You can run your own, as well


Finding Images

- `docker search` command


Story Time

- Clean up your images regularly. You will discover the images you really need to keep
- Be aware of how much you are trusting the containers you fetch
```
