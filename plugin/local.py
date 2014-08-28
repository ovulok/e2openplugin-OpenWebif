# -*- coding: utf-8 -*-

from __init__ import _

tstrings = {'mo': _("Mo"),
	'tu': _("Tu"),
	'we': _("We"),
	'th': _("Th"),
	'fr': _("Fr"),
	'sa': _("Sa"),
	'su': _("Su"),

	'day_0': _("Sun"),
	'day_1': _("Mon"),
	'day_2': _("Tue"),
	'day_3': _("Wed"),
	'day_4': _("Thu"),
	'day_5': _("Fri"),
	'day_6': _("Sat"),

	'monday': _("Monday"),
	'tuesday': _("Tuesday"),
	'wednesday': _("Wednesday"),
	'thursday': _("Thursday"),
	'friday': _("Friday"),
	'saturday': _("Saturday"),
	'sunday': _("Sunday"),

	'month_01': _("January"),
	'month_02': _("February"),
	'month_03': _("March"),
	'month_04': _("April"),
	'month_05': _("May"),
	'month_06': _("June"),
	'month_07': _("July"),
	'month_08': _("August"),
	'month_09': _("September"),
	'month_10': _("October"),
	'month_11': _("November"),
	'month_12': _("December"),

	'about': _("About"),
	'add_timer': _("Add Timer"),
	'add_autotimer': _("Add AutoTimer"),
	'add_zaptimer': _("Add Zap Timer"),
	'after_event': _("After Event"),
	'agc': _("AGC"),
	'all': _("All"),
	'all_channels': _("All Channels"),
	'authors': _("Authors"),
	'auto': _("Auto"),
	'back': _("Back"),
	'begin': _("Begin"),
	'ber': _("BER"),
	'bouquets': _("Bouquets"),
	'box_info': _("Box Info"),
	'box': _("Box"),
	'boxcontrol': _("Box Control"),
	'box_uptime': _("Box Uptime"),
	'brand': _("Brand"),
	'cancel': _("Cancel"),
	'capacity': _("Capacity"),
	'channel': _("Channel"),
	'channels': _("Channels"),
	'chipset': _("Chipset"),
	'cleanup_timer':_("Cleanup Timers"),
	'contributors': _("Contributors"),
	'control': _("Control"),
	'current': _("Current"),
	'current_event': _("Current Event"),
	'deep_standby': _("Deep-Standby"),
	'default': _("Default"),
	'delete_recording': _("Delete Recording"),
	'delete_recording_question': _("Really delete the recording"),
	'delete_movie': _("Delete Movie"),
	'delete_movie_question': _("Really delete the movie"),
	'delete_timer': _("Delete Timer"),
	'delete_timer_question': _("Really delete the timer"),
	'description': _("Description"),
	'dhcp': _("DHCP"),
	'disable_timer': _("Disable Timer"),
	'distro_version': _("Distro"),
	'dolby': _("Dolby"),
	'done': _("Done"),
	'download': _("Download"),
	'download_playlist': _("Download Playlist for"),
	'driver_date': _("Driver date"),
	'duration': _("Duration"),
	'edit_timer': _("Edit Timer"),
	'enable_timer': _("Enable Timer"),
	'start': _("Start"),
	'end': _("End"),
	'enabled': _("Enabled"),
	'encrypted': _("Encrypted"),
	'epg': _("EPG"),
	'epgsearch': _("Epg Search"),
	'error': _("Error"),
	'every_timer': _("Every"),
	'extras': _("Extras"),
	'finished': _("finished"),
	'firmware_version': _("Firmware version"),
	'fp_version': _("Frontprocessor Version"),
	'free': _("Free"),
	'free_memory': _("Free Memory"),
	'gateway': _("Gateway"),
	'grabscreenshot': _("Grab Screenshot"),
	'gui_version': _("Gui version"),
	'hidefullremote': _("Hide full remote"),
	'high_resolution': _("High Resolution"),
	'hdd_model': _("Hard disk model"),
	'hour': _("Hour"),
	'ip_address': _("IP address"),
	'ipv4only_kernel': _("IPv4-only kernel"),
	'ipv4only_network': _("none/IPv4-only network"),
	'ipv4only_python': _("IPv4-only Python/Twisted"),
	'ipv6_address': _("IPv6 address(es)"),
	'info': _("Infos"),
	'instant_record': _("Instant Record"),
	'javalib': _("Javascript Libraries"),
	'just_play': _("Just play"),
	'kernel_version': _("Kernel version"),
	'license': _("LICENSE"),
	'loading': _("loading"),
	'location': _("Location"),
	'locked': _("Locked"),
	'mac_address': _("MAC address"),
	'main': _("Main"),
	'minute': _("Minute"),
	'model': _("Model"),
	'movielist': _("Movielist"),
	'movies': _("Movies"),
	'multi_epg': _("MultiEPG"),
	'name': _("Name"),
	'namespace': _("Namespace"),
	'network_interface': _("Network Interface"),
	'no_description_available': _("no description available"),
	'not_implemented': _("Sorry this page is not yet implemented"),
	'nothing': _("Nothing"),
	'nothing_play': _("Nothing playing."),
	'now': _("Now"),
	'oe_version': _("System OE"),
	'on': _("On"),
	'openwebif_header': _("Open Source Web Interface for Linux set-top box"),
	'osd': _("OSD"),
	'playback': _("Playback"),
	'playlist': _("Playlist"),
	'powercontrol': _("Power Control"),
	'provider': _("Provider"),
	'providers': _("Providers"),
	'radio': _("Radio"),
	'reboot_box': _("Reboot Box"),
	'rec_status': _("Recording Status"),
	'refresh': _("Refresh"),
	'refresh_auto': _("Refresh automatically every"),
	'refresh_timer': _("Refresh Timer"),
	'remote': _("Remote"),
	'rename_recording': _("Rename Recording"),
	'repeated': _("Repeated"),
	'restart_gui': _("Restart GUI"),
	'running': _("running"),
	'satellites': _("Satellites"),
	'satfinder': _("Satfinder"),
	'save': _("Save"),
	'screenshot': _("Screenshot"),
	'search': _("Search"),
	'search_imdb': _("Search IMDb"),
	'seconds': _("seconds"),
	'send_message': _("Send Message"),
	'sent_wait': _('Waiting for answer ...'),
	'sendamessage': _("Send a Message"),
	'service': _("Service"),
	'settings': _("Settings"),
	'Bouquet_Editor': _("Bouquet Editor"),
	'shiftforlong': _("(shift + click for long pressure)"),
	'show_full_openwebif': _("Show Full OpenWebif"),
	'showfullremote': _("Show full remote"),
	'show_epg_for': _("Show EPG for"),
	'shutdown': _("Shutdown"),
	'site_source': _("Site and sources"),
	'snr': _("SNR"),
	'software': _("Software"),
	'standby': _("Standby"),
	'standby_toggle': _("Standby Toggle"),
	'start_after_end': _("Start time is after end time"),
	'start_instant_record': _("Start Instant Record"),
	'stream': _("Stream"),
	'subnet_mask': _("Subnet mask"),
	'subservices': _("Subservices"),
	'tags': _("Tags"),
	'teletext': _("Teletext"),
	'television': _("Television"),
	'template_engine': _("Template Engine"),
	'text': _("Text"),
	'time': _("Time"),
	'timeout': _("Timeout"),
	'timer_added': _("Timer added"),
	'timer_list': _("Timerlist"),
	'timer_newname': _("New Name"),
	'timer_preview': _("Autotimer Preview"),
	'timer': _("Timer"),
	'timers': _("Timers"),
	'title': _("Title"),
	'total_memory': _("Total Memory"),
	'transcode': _("Transcode"),
	'tuner_ber': _("Tuner Bit Error Rate BER"),
	'tuner_number': _("Tuner Number (0-3)"),
	'tuner_signal': _("Tuner Signal"),
	'tuner_signal_snr': _("Tuner Signal Quality SNR"),
	'tuner_signal_snr_db': _("Tuner Signal Quality SNR_DB"),
	'tuner_signal_agc': _("Tuner Signal Power AGC"),
	'tuner_type': _("Tuner Type"),
	'tuners': _("Tuners"),
	'tv': _("TV"),
	'tv_multi_epg': _("TV Multi EPG"),
	'type': _("Type"),
	'upcoming_events': _("Upcoming Events"),
	'version': _("Version"),
	'video': _("Video"),
	'video_height': _("Video Height"),
	'video_wide': _("Video Wide"),
	'video_width': _("Video Width"),
	'volume': _("Volume"),
	'volumecontrol': _("Volume Control"),
	'waiting': _("waiting"),
	'warning': _("Warning"),
	'yes_no': _("Yes/No"),
	'zap': _("Zap"),
	'zapbeforestream': _("zap before Stream"),
	'zap_to': _("Zap to"),
	'zapped_to': _("Zapped to"),
	'translation_spanish': _('Translation to Spanish'),
	'license_text_01': _('All Files of this Software are open source software;'),
	'license_text_02': _('you can redistribute it and/or modify it under the'),
	'license_text_03': _('terms of the GNU General Public License version 2 as'),
	'license_text_04': _('published by the Free Software Foundation.'),
	'license_text_m': _('All Files of this Software are open source software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 2 as published by the Free Software Foundation.'),
	'Root': _('Root'),

	'at_list': _("AutoTimer List"),
	'at_at_edit': _("AutoTimer Edit"),
	'at_enabled': _("Enabled"),
	'at_description': _("Description"),
	'at_title_match': _("Match title"),
	'at_encoding': _("EPG encoding"),
	'at_search_type': _("Search type"),
	'at_partial_match': _("partial match"),
	'at_exact_match': _("exact match"),
	'at_description_match': _("description match"),
	'at_start_match': _("start match"),
	'at_search_strictness': _("Search strictness"),
	'at_case_sensitive': _("case-sensitive search"),
	'at_case_insensitive': _("case-insensitive search"),
	'at_timer_type': _("Timer type"),
	'at_record': _("record"),
	'at_zap': _("zap"),
	'at_override_alt': _("Override found with alternative service"),
	'at_timespan': _("Only match during timespan"),
	'at_timespan_begin': _("Begin of timespan"),
	'at_timespan_end': _("End of Timespan"),
	'at_datespan': _("Restrict to events on certain dates"),
	'at_datespan_after': _("Not after"),
	'at_datespan_before': _("Not before"),
	'at_timer_offset': _("Custom offset"),
	'at_timer_offset_before': _("Offset before recording (in m)"),
	'at_timer_offset_after': _("Offset after recording (in m)"),
	'at_max_duration': _("Set maximum duration"),
	'at_after_event': _("After event"),
	'at_after_event_standard': _("standard"),
	'at_after_event_auto': _("auto"),
	'at_after_event_nothing': _("do nothing"),
	'at_after_event_standby': _("go to standby"),
	'at_after_event_deepstandby': _("go to deep standby"),
	'at_event_timespan': _('Execute "after event" during timespan'),
	'at_event_timespan_begin': _('Begin of "after event" timespan'),
	'at_event_timespan_end': _('End of "after event" timespan'),
	'at_max_counter': _("Record a maximum of x times"),
	'at_left': _("Amount of recordings left"),
	'at_never': _("Never"),
	'at_monthly': _("Monthly"),
	'at_weekly_sun': _("Weekly (Sunday)"),
	'at_weekly_mon': _("Weekly (Monday)"),
	'at_reset_count': _("Reset count"),
	'at_avoid_dup': _("Require description to be unique"),
	'at_avoid_dup_no': _("No"),
	'at_avoid_dup_same_service': _("On same service"),
	'at_avoid_dup_any_service': _("On any service"),
	'at_avoid_dup_any_service_rec': _("Any service/recording"),
	'at_location': _("Use a custom location"),
	'at_tags': _("Tags"),
	'at_select_tags': _("select Tags"),
	'at_channels': _("Channels"),
	'at_select_channels': _("select Channels"),
	'at_bouquets': _("Bouquets"),
	'at_select_bouquets': _("select Bouquets"),
	'at_filter': _("Enable Filtering"),
	'at_filter_include': _("Include"),
	'at_filter_exclude': _("Exclude"),
	'at_filter_title': _("in Title"),
	'at_filter_short_desc': _("in Shortdescription"),
	'at_filter_desc': _("in Description"),
	'at_filter_day': _("on Weekday"),
	'at_filter_weekend': _("Weekend"),
	'at_filter_weekday': _("Weekday"),
	'at_vps': _("VPS"),
	'at_vps_override': _("VPS Overwrite"),
	'at_add': _("Add"),
	'at_del': _("Delete"),
	'at_reload': _("Reload"),
	'at_save': _("Save"),
	'at_parse': _("Parse"),
	'at_simulate': _("Simulate"),
	'at_timers': _("Timers"),
	'at_delete_autotimer_question': _("Do you really want to delete the AT"),
	'at_label_series': _("Label series"),

	'bqe_add_provider_as_bouquet': _("Add Provider as new Bouquet"),
	'bqe_add_channel': _("Add channel(s) to Bouquet"),
	'bqe_add_alternative': _("Add channel(s) as alternate"),
	'bqe_search': _("Search"),
	'bqe_reload': _("Reload"),
	'bqe_export': _("Export"),
	'bqe_import': _("Import"),
	'bqe_add_bq': _("Add Bouquet"),
	'bqe_rename_bq': _("Rename Bouquet"),
	'bqe_delete_bq': _("Delete Bouquet"),
	'bqe_add_marker': _("Add Marker"),
	'bqe_rename': _("Rename"),
	'bqe_delete_channel': _("Delete Channel(s)"),
	'bqe_del_channel_question': _("Do you really want to delete the channel(s)"),
	'bqe_del_bouquet_question': _("Do you really want to delete the bouquet"),
	'bqe_name_bouquet': _("Name of the Bouquet"),
	'bqe_name_marker': _("Name of the Marker"),
	'bqe_rename_bouquet': _("Enter new name for the bouquet"),
	'bqe_rename_marker': _("Enter new name for the marker"),
	'bqe_filename': _("Please enter filename"),
	'bqe_restore_question': _("Do you really want to restore from file"),

 	}
