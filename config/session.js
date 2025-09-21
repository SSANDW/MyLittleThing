const session = require('express-session');
const mysqlStore = require('express-mysql-session')(session);
const mysql = require('mysql2/promise');

function createSessionStore() {
    const sessionStore = new mysqlStore({
        host: 'localhost',
        user: 'root',
        password: 'skdml@100',
        database: 'myproject'
    });

    return sessionStore;
};

function createSessionConfig() {
    return {
        key: 'cookcook',
        secret: 'super-secret',
        store: createSessionStore(),
        resave: false,
        saveUninitialized: false,
        cookie: {
            maxAge: 1000 * 60 * 3
        }
    }
};

module.exports = createSessionConfig