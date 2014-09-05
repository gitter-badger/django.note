# coding: utf-8

import sys
import codecs
import django
import uuid
import json
import logging
import subprocess
import datetime
import time
import inspect
import project1
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext
from app1.utils import *
from app1.form import *
from django.contrib.auth.decorators import login_required

# Create your views here.

logger = logging.getLogger(__name__)

# out = codecs.getwriter('utf-8')(sys.stdout)

@login_required
def default(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# デフォルトページのアクション
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup
	# =========================================================================

	# =========================================================================
	# validation
	# =========================================================================

	# =========================================================================
	# process
	# =========================================================================
	
	# =========================================================================
	# contents
	# =========================================================================
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	fields = {}
	fields['window_title'] = 'HOME'
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('floatings/default.html')
	return django.http.HttpResponse(template.render(context))
