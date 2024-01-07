#!/usr/bin/node
const firstArg = require('fs');
const a = firstArg.readFileSync(process.argv[2], 'utf8');
const b = firstArg.readFileSync(process.argv[3], 'utf8');
firstArg.writeFileSync(process.argv[4], a + b);
