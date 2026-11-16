const express = require('express');

const app = express();

app.use(express.json());

let students = [
    { id: 1, name: "Rahul" },
    { id: 2, name: "Priya" }
];