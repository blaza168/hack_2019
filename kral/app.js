const express = require('express');

const http = require('http');

const fs = require('fs');

const url = "http://10.10.10.241:5000";

let image;

http.get(url, res => {
    //res.setEncoding("utf8");
    res.on("data", data => {
        console.log(data);

    });


});

const app = express();

const PORT = 5000

//app.use(require('./routes/index'));


//app.listen(PORT);