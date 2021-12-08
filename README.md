# Local environment for a cloud function
Build the cloud function container
```
make build
```

Run the cloud function locally
```
make run
```

Execute the funtion locally
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"name": "Jack", "last_name": "Pearson"}'
```

Run the tests
```
make test
```