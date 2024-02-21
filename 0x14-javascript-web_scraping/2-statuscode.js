#!/usr/bin/node

const request = require('require');

request(process.argv[2], function (_err, res) {
    console.log('code:', res.statusCode);
});