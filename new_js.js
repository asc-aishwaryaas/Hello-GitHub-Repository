const express = require('express');

const app = express();

app.get('/students', (req, res) => {
    res.json({ message: "Students data" });
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
