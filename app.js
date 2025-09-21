const path = require('path');

const express = require("express");
const csrf = require('csurf');

const sessionConfig = require('./config/session');
const addCsrfTokenMiddleware = require('./middlewares/csrf-token');
const authRoutes = require('./routes/auth.routes');
const errorHandlerMiddleware = require('./middlewares/error-handler');
const session = require('express-session');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, 'public')))

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(session(sessionConfig()));
app.use(csrf());

app.use(addCsrfTokenMiddleware);
app.use(authRoutes);

console.log(errorHandlerMiddleware);
app.use(errorHandlerMiddleware.handleErrors);

app.listen(3000);