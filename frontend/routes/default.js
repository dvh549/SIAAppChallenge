var express = require('express');
var router = express.Router();

//index route
router.get("/login", function(req, res) {
    res.render("index.ejs");
})

module.exports = router;