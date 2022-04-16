#!/usr/bin/python python3
# coding=utf-8
from . import main
from flask import redirect, url_for


@main.app_errorhandler(404)
def page_not_found(e):
    """注册应用全局错误处理"""
    print("404")
    return redirect(url_for('main.index'))


@main.app_errorhandler(401)
def authfail(e):
    return redirect('/static/401.jpg')