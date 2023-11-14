# importações 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import _find_elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import openpyxl
import smtplib
import os
from email.message import EmailMessage
import re

# aplicação
