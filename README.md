# Nas control
A simple API to start/stop programs on the nas

## Installation
Clone project
```

```

Install mplayer
```
apt-get install mplayer
```

Install python libs
```
pip install flask
```

Install system script
```
cp init_script/nas_control.service /etc/systemd/system/nas_control.service
systemctl daemon-reload
systemctl start nas_control
systemctl enable nas_control
```

## Usage
Test with curl

Access root page
```
curl -i -X GET --user admin:secret http://localhost:5000/
```

## App
Start Steam
```
curl -i --user admin:secret -H "Content-Type: application/json" -X POST -d '{"app_name":"steam","state":"start"}' http://localhost:5000/app
```

Stop Steam
```
curl -i --user admin:secret -H "Content-Type: application/json" -X POST -d '{"app_name":"steam","state":"stop"}' http://localhost:5000/app
```