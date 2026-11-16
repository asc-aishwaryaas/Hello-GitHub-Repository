const express = require('express');
const app = express();

app.use(express.json());

function logger(req, res, next) {
    console.log("Request received");
    console.log("Method:", req.method);
    console.log("URL:", req.url);
    next();
}

app.use(logger);

app.post('/students', (req, res) => {
    console.log("Inside route handler");
    const student = req.body;
    console.log("Student data:", student);
    res.json({
        message: "Student received",
        student: student
    });
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});