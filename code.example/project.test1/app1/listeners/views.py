# coding: utf-8

import django
import logging
import subprocess
import time
from app1.utils import *

logger = logging.getLogger(__name__)

def show(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# netstat �̏�Ԃ�\������A�N�V����
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('$$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug('�g�b�v�y�[�W�փ��_�C���N�g���܂��B')
		return django.http.HttpResponseRedirect('/')

	# =========================================================================
	# process
	# =========================================================================

	# current user
	user_name = request.session.get('user')
	# netstat �̐ݒ�����[�h
	listeners = util.listeners_list()

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['form'] = {
		'listeners': listeners,
	}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('listeners/show.html')
	logger.debug('�R���e���c��Ԃ��܂��B')
	return django.http.HttpResponse(template.render(context))

