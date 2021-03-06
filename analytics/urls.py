# analytics/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from . import views_admin
from django.conf.urls import url


urlpatterns = [
    # views_admin
    url(r'^$', views_admin.analytics_index_view, name='analytics_index',),
    url(r'^analytics_index_process/$',
        views_admin.analytics_index_process_view, name='analytics_index_process'),
    url(r'^analytics_action_list/(?P<voter_we_vote_id>wv[\w]{2}voter[\w]+)/$',
        views_admin.analytics_action_list_view, name='analytics_action_list'),
    url(r'^analytics_action_list/(?P<organization_we_vote_id>wv[\w]{2}org[\w]+)/$',
        views_admin.analytics_action_list_view, name='analytics_action_list'),
    url(r'^analytics_action_list/(?P<incorrect_integer>[0-9]+)/$',
        views_admin.analytics_action_list_view, name='analytics_action_list'),  # Needed for bug with bad data
    url(r'^analytics_action_list/$',
        views_admin.analytics_action_list_view, name='analytics_action_list'),
    url(r'^augment_voter_analytics_process/(?P<voter_we_vote_id>wv[\w]{2}voter[\w]+)/$',
        views_admin.augment_voter_analytics_process_view, name='augment_voter_analytics_process'),
    url(r'^organization_analytics_index/$',
        views_admin.organization_analytics_index_view, name='organization_analytics_index',),
    url(r'^organization_daily_metrics/$',
        views_admin.organization_daily_metrics_view, name='organization_daily_metrics'),
    url(r'^organization_daily_metrics_process/$',
        views_admin.organization_daily_metrics_process_view, name='organization_daily_metrics_process'),
    url(r'^organization_election_metrics/$',
        views_admin.organization_election_metrics_view, name='organization_election_metrics'),
    url(r'^organization_election_metrics_process/$',
        views_admin.organization_election_metrics_process_view, name='organization_election_metrics_process'),
    url(r'^sitewide_daily_metrics/$', views_admin.sitewide_daily_metrics_view, name='sitewide_daily_metrics'),
    url(r'^sitewide_daily_metrics_process/$',
        views_admin.sitewide_daily_metrics_process_view, name='sitewide_daily_metrics_process'),
    url(r'^sitewide_election_metrics/$', views_admin.sitewide_election_metrics_view, name='sitewide_election_metrics'),
    url(r'^sitewide_election_metrics_process/$',
        views_admin.sitewide_election_metrics_process_view, name='sitewide_election_metrics_process'),
    url(r'^sitewide_voter_metrics/$', views_admin.sitewide_voter_metrics_view, name='sitewide_voter_metrics'),
    url(r'^sitewide_voter_metrics_process/$',
        views_admin.sitewide_voter_metrics_process_view, name='sitewide_voter_metrics_process'),
]
