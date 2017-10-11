from flask import Flask, url_for, render_template, request, make_response, redirect
import json
from portal import app
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans'


class Render(object):
    def __init__(self, status, data):
        self.status = status
        self.message = data
        self.data = self.render_json()

    def render_json(self):
        return json.dumps({'status': self.status, 'message': self.message})


class RenderData(Render):
    def __init__(self, status, data):
        super(RenderData, self).__init__(status, data)


def render_json(status, data):
    message = RenderData(status, data)
    return message.data


def render_200(data=None):
    message = render_json(200, data)
    return message


def render_400(data=None):
    message = render_json(400, data)
    return message


def render_404(data=None):
    message = render_json(404, data)
    return message


def render_500(data=None):
    message = render_json(500, data)
    return message
