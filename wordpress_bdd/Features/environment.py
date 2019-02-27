from selenium import webdriver
import time

def before_feature(context):
    context.dr = webdriver.Firefox()


def after_feature(context):
    context.dr.close()


def after_step(context, step):
    context.dr.save_screenshot('./%s%s.png' %(time.time(), step))