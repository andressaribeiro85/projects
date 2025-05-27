import pytest
from project import brightness
from project import brightness_range
from project import color_avg
from project import img_size

img_test = "image_test.jpg"

def test_brightness():
    assert brightness(img_test) == 0.38905037625776817

def test_brightness_range():
    assert brightness_range(img_test) == (1, 255)

def test_color_avg():
    assert color_avg(img_test) == 1.0

def test_img_size():
    assert img_size(img_test) == (284, 177)


