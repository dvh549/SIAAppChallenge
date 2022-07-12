var express = require('express');
var router = express.Router();

//index route
router.get("/", function(req, res) {
    res.render("index.ejs");
})

module.exports = router;