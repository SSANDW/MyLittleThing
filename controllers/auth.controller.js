const db = require('../data/database');
const userModel = require('../models/user.model');

function getSignup(req, res) {
 res.render('customer/auth/signup');
}

async function signup(req, res) {

    const email = req.body.email;
    const password = req.body.password;
    const name = req.body.fullname;
    const street = req.body.street;
    const postal = req.body.postal;
    const city = req.body.city;

    const user = new userModel(email, password, name, street, postal, city);
    await user.signup();

    res.redirect('/login');
}

function getLogin(req, res) {
    res.render('customer/auth/login');
}

module.exports = {
    signup: signup,
    getSignup: getSignup,
    getLogin: getLogin
};