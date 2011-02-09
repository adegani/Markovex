# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _sequencer_alsa
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


open_client = _sequencer_alsa.open_client
new_port_subscribe = _sequencer_alsa.new_port_subscribe
new_queue_status = _sequencer_alsa.new_queue_status
free_queue_status = _sequencer_alsa.free_queue_status
new_port_info = _sequencer_alsa.new_port_info
new_client_info = _sequencer_alsa.new_client_info
event_input = _sequencer_alsa.event_input
snd_seq_control_queue_eventless = _sequencer_alsa.snd_seq_control_queue_eventless
init_queue_tempo = _sequencer_alsa.init_queue_tempo
client_poll_descriptors = _sequencer_alsa.client_poll_descriptors
SND_SEQ_OPEN_OUTPUT = _sequencer_alsa.SND_SEQ_OPEN_OUTPUT
SND_SEQ_OPEN_INPUT = _sequencer_alsa.SND_SEQ_OPEN_INPUT
SND_SEQ_OPEN_DUPLEX = _sequencer_alsa.SND_SEQ_OPEN_DUPLEX
SND_SEQ_NONBLOCK = _sequencer_alsa.SND_SEQ_NONBLOCK
SND_SEQ_TYPE_HW = _sequencer_alsa.SND_SEQ_TYPE_HW
SND_SEQ_TYPE_SHM = _sequencer_alsa.SND_SEQ_TYPE_SHM
SND_SEQ_TYPE_INET = _sequencer_alsa.SND_SEQ_TYPE_INET
SND_SEQ_ADDRESS_UNKNOWN = _sequencer_alsa.SND_SEQ_ADDRESS_UNKNOWN
SND_SEQ_ADDRESS_SUBSCRIBERS = _sequencer_alsa.SND_SEQ_ADDRESS_SUBSCRIBERS
SND_SEQ_ADDRESS_BROADCAST = _sequencer_alsa.SND_SEQ_ADDRESS_BROADCAST
SND_SEQ_CLIENT_SYSTEM = _sequencer_alsa.SND_SEQ_CLIENT_SYSTEM
SND_SEQ_CLIENT_DUMMY = _sequencer_alsa.SND_SEQ_CLIENT_DUMMY
SND_SEQ_CLIENT_OSS = _sequencer_alsa.SND_SEQ_CLIENT_OSS
snd_seq_open = _sequencer_alsa.snd_seq_open
snd_seq_open_lconf = _sequencer_alsa.snd_seq_open_lconf
snd_seq_name = _sequencer_alsa.snd_seq_name
snd_seq_type = _sequencer_alsa.snd_seq_type
snd_seq_close = _sequencer_alsa.snd_seq_close
snd_seq_poll_descriptors_count = _sequencer_alsa.snd_seq_poll_descriptors_count
snd_seq_poll_descriptors = _sequencer_alsa.snd_seq_poll_descriptors
snd_seq_poll_descriptors_revents = _sequencer_alsa.snd_seq_poll_descriptors_revents
snd_seq_nonblock = _sequencer_alsa.snd_seq_nonblock
snd_seq_client_id = _sequencer_alsa.snd_seq_client_id
snd_seq_get_output_buffer_size = _sequencer_alsa.snd_seq_get_output_buffer_size
snd_seq_get_input_buffer_size = _sequencer_alsa.snd_seq_get_input_buffer_size
snd_seq_set_output_buffer_size = _sequencer_alsa.snd_seq_set_output_buffer_size
snd_seq_set_input_buffer_size = _sequencer_alsa.snd_seq_set_input_buffer_size
snd_seq_system_info_sizeof = _sequencer_alsa.snd_seq_system_info_sizeof
snd_seq_system_info_malloc = _sequencer_alsa.snd_seq_system_info_malloc
snd_seq_system_info_free = _sequencer_alsa.snd_seq_system_info_free
snd_seq_system_info_copy = _sequencer_alsa.snd_seq_system_info_copy
snd_seq_system_info_get_queues = _sequencer_alsa.snd_seq_system_info_get_queues
snd_seq_system_info_get_clients = _sequencer_alsa.snd_seq_system_info_get_clients
snd_seq_system_info_get_ports = _sequencer_alsa.snd_seq_system_info_get_ports
snd_seq_system_info_get_channels = _sequencer_alsa.snd_seq_system_info_get_channels
snd_seq_system_info_get_cur_clients = _sequencer_alsa.snd_seq_system_info_get_cur_clients
snd_seq_system_info_get_cur_queues = _sequencer_alsa.snd_seq_system_info_get_cur_queues
snd_seq_system_info = _sequencer_alsa.snd_seq_system_info
SND_SEQ_USER_CLIENT = _sequencer_alsa.SND_SEQ_USER_CLIENT
SND_SEQ_KERNEL_CLIENT = _sequencer_alsa.SND_SEQ_KERNEL_CLIENT
snd_seq_client_info_sizeof = _sequencer_alsa.snd_seq_client_info_sizeof
snd_seq_client_info_malloc = _sequencer_alsa.snd_seq_client_info_malloc
snd_seq_client_info_free = _sequencer_alsa.snd_seq_client_info_free
snd_seq_client_info_copy = _sequencer_alsa.snd_seq_client_info_copy
snd_seq_client_info_get_client = _sequencer_alsa.snd_seq_client_info_get_client
snd_seq_client_info_get_type = _sequencer_alsa.snd_seq_client_info_get_type
snd_seq_client_info_get_name = _sequencer_alsa.snd_seq_client_info_get_name
snd_seq_client_info_get_broadcast_filter = _sequencer_alsa.snd_seq_client_info_get_broadcast_filter
snd_seq_client_info_get_error_bounce = _sequencer_alsa.snd_seq_client_info_get_error_bounce
snd_seq_client_info_get_event_filter = _sequencer_alsa.snd_seq_client_info_get_event_filter
snd_seq_client_info_get_num_ports = _sequencer_alsa.snd_seq_client_info_get_num_ports
snd_seq_client_info_get_event_lost = _sequencer_alsa.snd_seq_client_info_get_event_lost
snd_seq_client_info_set_client = _sequencer_alsa.snd_seq_client_info_set_client
snd_seq_client_info_set_name = _sequencer_alsa.snd_seq_client_info_set_name
snd_seq_client_info_set_broadcast_filter = _sequencer_alsa.snd_seq_client_info_set_broadcast_filter
snd_seq_client_info_set_error_bounce = _sequencer_alsa.snd_seq_client_info_set_error_bounce
snd_seq_client_info_set_event_filter = _sequencer_alsa.snd_seq_client_info_set_event_filter
snd_seq_get_client_info = _sequencer_alsa.snd_seq_get_client_info
snd_seq_get_any_client_info = _sequencer_alsa.snd_seq_get_any_client_info
snd_seq_set_client_info = _sequencer_alsa.snd_seq_set_client_info
snd_seq_query_next_client = _sequencer_alsa.snd_seq_query_next_client
snd_seq_client_pool_sizeof = _sequencer_alsa.snd_seq_client_pool_sizeof
snd_seq_client_pool_malloc = _sequencer_alsa.snd_seq_client_pool_malloc
snd_seq_client_pool_free = _sequencer_alsa.snd_seq_client_pool_free
snd_seq_client_pool_copy = _sequencer_alsa.snd_seq_client_pool_copy
snd_seq_client_pool_get_client = _sequencer_alsa.snd_seq_client_pool_get_client
snd_seq_client_pool_get_output_pool = _sequencer_alsa.snd_seq_client_pool_get_output_pool
snd_seq_client_pool_get_input_pool = _sequencer_alsa.snd_seq_client_pool_get_input_pool
snd_seq_client_pool_get_output_room = _sequencer_alsa.snd_seq_client_pool_get_output_room
snd_seq_client_pool_get_output_free = _sequencer_alsa.snd_seq_client_pool_get_output_free
snd_seq_client_pool_get_input_free = _sequencer_alsa.snd_seq_client_pool_get_input_free
snd_seq_client_pool_set_output_pool = _sequencer_alsa.snd_seq_client_pool_set_output_pool
snd_seq_client_pool_set_input_pool = _sequencer_alsa.snd_seq_client_pool_set_input_pool
snd_seq_client_pool_set_output_room = _sequencer_alsa.snd_seq_client_pool_set_output_room
snd_seq_get_client_pool = _sequencer_alsa.snd_seq_get_client_pool
snd_seq_set_client_pool = _sequencer_alsa.snd_seq_set_client_pool
SND_SEQ_PORT_SYSTEM_TIMER = _sequencer_alsa.SND_SEQ_PORT_SYSTEM_TIMER
SND_SEQ_PORT_SYSTEM_ANNOUNCE = _sequencer_alsa.SND_SEQ_PORT_SYSTEM_ANNOUNCE
SND_SEQ_PORT_CAP_READ = _sequencer_alsa.SND_SEQ_PORT_CAP_READ
SND_SEQ_PORT_CAP_WRITE = _sequencer_alsa.SND_SEQ_PORT_CAP_WRITE
SND_SEQ_PORT_CAP_SYNC_READ = _sequencer_alsa.SND_SEQ_PORT_CAP_SYNC_READ
SND_SEQ_PORT_CAP_SYNC_WRITE = _sequencer_alsa.SND_SEQ_PORT_CAP_SYNC_WRITE
SND_SEQ_PORT_CAP_DUPLEX = _sequencer_alsa.SND_SEQ_PORT_CAP_DUPLEX
SND_SEQ_PORT_CAP_SUBS_READ = _sequencer_alsa.SND_SEQ_PORT_CAP_SUBS_READ
SND_SEQ_PORT_CAP_SUBS_WRITE = _sequencer_alsa.SND_SEQ_PORT_CAP_SUBS_WRITE
SND_SEQ_PORT_CAP_NO_EXPORT = _sequencer_alsa.SND_SEQ_PORT_CAP_NO_EXPORT
SND_SEQ_PORT_TYPE_SPECIFIC = _sequencer_alsa.SND_SEQ_PORT_TYPE_SPECIFIC
SND_SEQ_PORT_TYPE_MIDI_GENERIC = _sequencer_alsa.SND_SEQ_PORT_TYPE_MIDI_GENERIC
SND_SEQ_PORT_TYPE_MIDI_GM = _sequencer_alsa.SND_SEQ_PORT_TYPE_MIDI_GM
SND_SEQ_PORT_TYPE_MIDI_GS = _sequencer_alsa.SND_SEQ_PORT_TYPE_MIDI_GS
SND_SEQ_PORT_TYPE_MIDI_XG = _sequencer_alsa.SND_SEQ_PORT_TYPE_MIDI_XG
SND_SEQ_PORT_TYPE_MIDI_MT32 = _sequencer_alsa.SND_SEQ_PORT_TYPE_MIDI_MT32
SND_SEQ_PORT_TYPE_SYNTH = _sequencer_alsa.SND_SEQ_PORT_TYPE_SYNTH
SND_SEQ_PORT_TYPE_DIRECT_SAMPLE = _sequencer_alsa.SND_SEQ_PORT_TYPE_DIRECT_SAMPLE
SND_SEQ_PORT_TYPE_SAMPLE = _sequencer_alsa.SND_SEQ_PORT_TYPE_SAMPLE
SND_SEQ_PORT_TYPE_APPLICATION = _sequencer_alsa.SND_SEQ_PORT_TYPE_APPLICATION
snd_seq_port_info_sizeof = _sequencer_alsa.snd_seq_port_info_sizeof
snd_seq_port_info_malloc = _sequencer_alsa.snd_seq_port_info_malloc
snd_seq_port_info_free = _sequencer_alsa.snd_seq_port_info_free
snd_seq_port_info_copy = _sequencer_alsa.snd_seq_port_info_copy
snd_seq_port_info_get_client = _sequencer_alsa.snd_seq_port_info_get_client
snd_seq_port_info_get_port = _sequencer_alsa.snd_seq_port_info_get_port
snd_seq_port_info_get_addr = _sequencer_alsa.snd_seq_port_info_get_addr
snd_seq_port_info_get_name = _sequencer_alsa.snd_seq_port_info_get_name
snd_seq_port_info_get_capability = _sequencer_alsa.snd_seq_port_info_get_capability
snd_seq_port_info_get_type = _sequencer_alsa.snd_seq_port_info_get_type
snd_seq_port_info_get_midi_channels = _sequencer_alsa.snd_seq_port_info_get_midi_channels
snd_seq_port_info_get_midi_voices = _sequencer_alsa.snd_seq_port_info_get_midi_voices
snd_seq_port_info_get_synth_voices = _sequencer_alsa.snd_seq_port_info_get_synth_voices
snd_seq_port_info_get_read_use = _sequencer_alsa.snd_seq_port_info_get_read_use
snd_seq_port_info_get_write_use = _sequencer_alsa.snd_seq_port_info_get_write_use
snd_seq_port_info_get_port_specified = _sequencer_alsa.snd_seq_port_info_get_port_specified
snd_seq_port_info_get_timestamping = _sequencer_alsa.snd_seq_port_info_get_timestamping
snd_seq_port_info_get_timestamp_real = _sequencer_alsa.snd_seq_port_info_get_timestamp_real
snd_seq_port_info_get_timestamp_queue = _sequencer_alsa.snd_seq_port_info_get_timestamp_queue
snd_seq_port_info_set_client = _sequencer_alsa.snd_seq_port_info_set_client
snd_seq_port_info_set_port = _sequencer_alsa.snd_seq_port_info_set_port
snd_seq_port_info_set_addr = _sequencer_alsa.snd_seq_port_info_set_addr
snd_seq_port_info_set_name = _sequencer_alsa.snd_seq_port_info_set_name
snd_seq_port_info_set_capability = _sequencer_alsa.snd_seq_port_info_set_capability
snd_seq_port_info_set_type = _sequencer_alsa.snd_seq_port_info_set_type
snd_seq_port_info_set_midi_channels = _sequencer_alsa.snd_seq_port_info_set_midi_channels
snd_seq_port_info_set_midi_voices = _sequencer_alsa.snd_seq_port_info_set_midi_voices
snd_seq_port_info_set_synth_voices = _sequencer_alsa.snd_seq_port_info_set_synth_voices
snd_seq_port_info_set_port_specified = _sequencer_alsa.snd_seq_port_info_set_port_specified
snd_seq_port_info_set_timestamping = _sequencer_alsa.snd_seq_port_info_set_timestamping
snd_seq_port_info_set_timestamp_real = _sequencer_alsa.snd_seq_port_info_set_timestamp_real
snd_seq_port_info_set_timestamp_queue = _sequencer_alsa.snd_seq_port_info_set_timestamp_queue
snd_seq_create_port = _sequencer_alsa.snd_seq_create_port
snd_seq_delete_port = _sequencer_alsa.snd_seq_delete_port
snd_seq_get_port_info = _sequencer_alsa.snd_seq_get_port_info
snd_seq_get_any_port_info = _sequencer_alsa.snd_seq_get_any_port_info
snd_seq_set_port_info = _sequencer_alsa.snd_seq_set_port_info
snd_seq_query_next_port = _sequencer_alsa.snd_seq_query_next_port
snd_seq_port_subscribe_sizeof = _sequencer_alsa.snd_seq_port_subscribe_sizeof
snd_seq_port_subscribe_malloc = _sequencer_alsa.snd_seq_port_subscribe_malloc
snd_seq_port_subscribe_free = _sequencer_alsa.snd_seq_port_subscribe_free
snd_seq_port_subscribe_copy = _sequencer_alsa.snd_seq_port_subscribe_copy
snd_seq_port_subscribe_get_sender = _sequencer_alsa.snd_seq_port_subscribe_get_sender
snd_seq_port_subscribe_get_dest = _sequencer_alsa.snd_seq_port_subscribe_get_dest
snd_seq_port_subscribe_get_queue = _sequencer_alsa.snd_seq_port_subscribe_get_queue
snd_seq_port_subscribe_get_exclusive = _sequencer_alsa.snd_seq_port_subscribe_get_exclusive
snd_seq_port_subscribe_get_time_update = _sequencer_alsa.snd_seq_port_subscribe_get_time_update
snd_seq_port_subscribe_get_time_real = _sequencer_alsa.snd_seq_port_subscribe_get_time_real
snd_seq_port_subscribe_set_sender = _sequencer_alsa.snd_seq_port_subscribe_set_sender
snd_seq_port_subscribe_set_dest = _sequencer_alsa.snd_seq_port_subscribe_set_dest
snd_seq_port_subscribe_set_queue = _sequencer_alsa.snd_seq_port_subscribe_set_queue
snd_seq_port_subscribe_set_exclusive = _sequencer_alsa.snd_seq_port_subscribe_set_exclusive
snd_seq_port_subscribe_set_time_update = _sequencer_alsa.snd_seq_port_subscribe_set_time_update
snd_seq_port_subscribe_set_time_real = _sequencer_alsa.snd_seq_port_subscribe_set_time_real
snd_seq_get_port_subscription = _sequencer_alsa.snd_seq_get_port_subscription
snd_seq_subscribe_port = _sequencer_alsa.snd_seq_subscribe_port
snd_seq_unsubscribe_port = _sequencer_alsa.snd_seq_unsubscribe_port
SND_SEQ_QUERY_SUBS_READ = _sequencer_alsa.SND_SEQ_QUERY_SUBS_READ
SND_SEQ_QUERY_SUBS_WRITE = _sequencer_alsa.SND_SEQ_QUERY_SUBS_WRITE
snd_seq_query_subscribe_sizeof = _sequencer_alsa.snd_seq_query_subscribe_sizeof
snd_seq_query_subscribe_malloc = _sequencer_alsa.snd_seq_query_subscribe_malloc
snd_seq_query_subscribe_free = _sequencer_alsa.snd_seq_query_subscribe_free
snd_seq_query_subscribe_copy = _sequencer_alsa.snd_seq_query_subscribe_copy
snd_seq_query_subscribe_get_client = _sequencer_alsa.snd_seq_query_subscribe_get_client
snd_seq_query_subscribe_get_port = _sequencer_alsa.snd_seq_query_subscribe_get_port
snd_seq_query_subscribe_get_root = _sequencer_alsa.snd_seq_query_subscribe_get_root
snd_seq_query_subscribe_get_type = _sequencer_alsa.snd_seq_query_subscribe_get_type
snd_seq_query_subscribe_get_index = _sequencer_alsa.snd_seq_query_subscribe_get_index
snd_seq_query_subscribe_get_num_subs = _sequencer_alsa.snd_seq_query_subscribe_get_num_subs
snd_seq_query_subscribe_get_addr = _sequencer_alsa.snd_seq_query_subscribe_get_addr
snd_seq_query_subscribe_get_queue = _sequencer_alsa.snd_seq_query_subscribe_get_queue
snd_seq_query_subscribe_get_exclusive = _sequencer_alsa.snd_seq_query_subscribe_get_exclusive
snd_seq_query_subscribe_get_time_update = _sequencer_alsa.snd_seq_query_subscribe_get_time_update
snd_seq_query_subscribe_get_time_real = _sequencer_alsa.snd_seq_query_subscribe_get_time_real
snd_seq_query_subscribe_set_client = _sequencer_alsa.snd_seq_query_subscribe_set_client
snd_seq_query_subscribe_set_port = _sequencer_alsa.snd_seq_query_subscribe_set_port
snd_seq_query_subscribe_set_root = _sequencer_alsa.snd_seq_query_subscribe_set_root
snd_seq_query_subscribe_set_type = _sequencer_alsa.snd_seq_query_subscribe_set_type
snd_seq_query_subscribe_set_index = _sequencer_alsa.snd_seq_query_subscribe_set_index
snd_seq_query_port_subscribers = _sequencer_alsa.snd_seq_query_port_subscribers
SND_SEQ_QUEUE_DIRECT = _sequencer_alsa.SND_SEQ_QUEUE_DIRECT
snd_seq_queue_info_sizeof = _sequencer_alsa.snd_seq_queue_info_sizeof
snd_seq_queue_info_malloc = _sequencer_alsa.snd_seq_queue_info_malloc
snd_seq_queue_info_free = _sequencer_alsa.snd_seq_queue_info_free
snd_seq_queue_info_copy = _sequencer_alsa.snd_seq_queue_info_copy
snd_seq_queue_info_get_queue = _sequencer_alsa.snd_seq_queue_info_get_queue
snd_seq_queue_info_get_name = _sequencer_alsa.snd_seq_queue_info_get_name
snd_seq_queue_info_get_owner = _sequencer_alsa.snd_seq_queue_info_get_owner
snd_seq_queue_info_get_locked = _sequencer_alsa.snd_seq_queue_info_get_locked
snd_seq_queue_info_get_flags = _sequencer_alsa.snd_seq_queue_info_get_flags
snd_seq_queue_info_set_name = _sequencer_alsa.snd_seq_queue_info_set_name
snd_seq_queue_info_set_owner = _sequencer_alsa.snd_seq_queue_info_set_owner
snd_seq_queue_info_set_locked = _sequencer_alsa.snd_seq_queue_info_set_locked
snd_seq_queue_info_set_flags = _sequencer_alsa.snd_seq_queue_info_set_flags
snd_seq_create_queue = _sequencer_alsa.snd_seq_create_queue
snd_seq_alloc_named_queue = _sequencer_alsa.snd_seq_alloc_named_queue
snd_seq_alloc_queue = _sequencer_alsa.snd_seq_alloc_queue
snd_seq_free_queue = _sequencer_alsa.snd_seq_free_queue
snd_seq_get_queue_info = _sequencer_alsa.snd_seq_get_queue_info
snd_seq_set_queue_info = _sequencer_alsa.snd_seq_set_queue_info
snd_seq_query_named_queue = _sequencer_alsa.snd_seq_query_named_queue
snd_seq_get_queue_usage = _sequencer_alsa.snd_seq_get_queue_usage
snd_seq_set_queue_usage = _sequencer_alsa.snd_seq_set_queue_usage
snd_seq_queue_status_sizeof = _sequencer_alsa.snd_seq_queue_status_sizeof
snd_seq_queue_status_malloc = _sequencer_alsa.snd_seq_queue_status_malloc
snd_seq_queue_status_free = _sequencer_alsa.snd_seq_queue_status_free
snd_seq_queue_status_copy = _sequencer_alsa.snd_seq_queue_status_copy
snd_seq_queue_status_get_queue = _sequencer_alsa.snd_seq_queue_status_get_queue
snd_seq_queue_status_get_events = _sequencer_alsa.snd_seq_queue_status_get_events
snd_seq_queue_status_get_tick_time = _sequencer_alsa.snd_seq_queue_status_get_tick_time
snd_seq_queue_status_get_real_time = _sequencer_alsa.snd_seq_queue_status_get_real_time
snd_seq_queue_status_get_status = _sequencer_alsa.snd_seq_queue_status_get_status
snd_seq_get_queue_status = _sequencer_alsa.snd_seq_get_queue_status
snd_seq_queue_tempo_sizeof = _sequencer_alsa.snd_seq_queue_tempo_sizeof
snd_seq_queue_tempo_malloc = _sequencer_alsa.snd_seq_queue_tempo_malloc
snd_seq_queue_tempo_free = _sequencer_alsa.snd_seq_queue_tempo_free
snd_seq_queue_tempo_copy = _sequencer_alsa.snd_seq_queue_tempo_copy
snd_seq_queue_tempo_get_queue = _sequencer_alsa.snd_seq_queue_tempo_get_queue
snd_seq_queue_tempo_get_tempo = _sequencer_alsa.snd_seq_queue_tempo_get_tempo
snd_seq_queue_tempo_get_ppq = _sequencer_alsa.snd_seq_queue_tempo_get_ppq
snd_seq_queue_tempo_get_skew = _sequencer_alsa.snd_seq_queue_tempo_get_skew
snd_seq_queue_tempo_get_skew_base = _sequencer_alsa.snd_seq_queue_tempo_get_skew_base
snd_seq_queue_tempo_set_tempo = _sequencer_alsa.snd_seq_queue_tempo_set_tempo
snd_seq_queue_tempo_set_ppq = _sequencer_alsa.snd_seq_queue_tempo_set_ppq
snd_seq_queue_tempo_set_skew = _sequencer_alsa.snd_seq_queue_tempo_set_skew
snd_seq_queue_tempo_set_skew_base = _sequencer_alsa.snd_seq_queue_tempo_set_skew_base
snd_seq_get_queue_tempo = _sequencer_alsa.snd_seq_get_queue_tempo
snd_seq_set_queue_tempo = _sequencer_alsa.snd_seq_set_queue_tempo
SND_SEQ_TIMER_ALSA = _sequencer_alsa.SND_SEQ_TIMER_ALSA
SND_SEQ_TIMER_MIDI_CLOCK = _sequencer_alsa.SND_SEQ_TIMER_MIDI_CLOCK
SND_SEQ_TIMER_MIDI_TICK = _sequencer_alsa.SND_SEQ_TIMER_MIDI_TICK
snd_seq_queue_timer_sizeof = _sequencer_alsa.snd_seq_queue_timer_sizeof
snd_seq_queue_timer_malloc = _sequencer_alsa.snd_seq_queue_timer_malloc
snd_seq_queue_timer_free = _sequencer_alsa.snd_seq_queue_timer_free
snd_seq_queue_timer_copy = _sequencer_alsa.snd_seq_queue_timer_copy
snd_seq_queue_timer_get_queue = _sequencer_alsa.snd_seq_queue_timer_get_queue
snd_seq_queue_timer_get_type = _sequencer_alsa.snd_seq_queue_timer_get_type
snd_seq_queue_timer_get_id = _sequencer_alsa.snd_seq_queue_timer_get_id
snd_seq_queue_timer_get_resolution = _sequencer_alsa.snd_seq_queue_timer_get_resolution
snd_seq_queue_timer_set_type = _sequencer_alsa.snd_seq_queue_timer_set_type
snd_seq_queue_timer_set_id = _sequencer_alsa.snd_seq_queue_timer_set_id
snd_seq_queue_timer_set_resolution = _sequencer_alsa.snd_seq_queue_timer_set_resolution
snd_seq_get_queue_timer = _sequencer_alsa.snd_seq_get_queue_timer
snd_seq_set_queue_timer = _sequencer_alsa.snd_seq_set_queue_timer
snd_seq_free_event = _sequencer_alsa.snd_seq_free_event
snd_seq_event_length = _sequencer_alsa.snd_seq_event_length
snd_seq_event_output = _sequencer_alsa.snd_seq_event_output
snd_seq_event_output_buffer = _sequencer_alsa.snd_seq_event_output_buffer
snd_seq_event_output_direct = _sequencer_alsa.snd_seq_event_output_direct
snd_seq_event_input = _sequencer_alsa.snd_seq_event_input
snd_seq_event_input_pending = _sequencer_alsa.snd_seq_event_input_pending
snd_seq_drain_output = _sequencer_alsa.snd_seq_drain_output
snd_seq_event_output_pending = _sequencer_alsa.snd_seq_event_output_pending
snd_seq_extract_output = _sequencer_alsa.snd_seq_extract_output
snd_seq_drop_output = _sequencer_alsa.snd_seq_drop_output
snd_seq_drop_output_buffer = _sequencer_alsa.snd_seq_drop_output_buffer
snd_seq_drop_input = _sequencer_alsa.snd_seq_drop_input
snd_seq_drop_input_buffer = _sequencer_alsa.snd_seq_drop_input_buffer
SND_SEQ_REMOVE_INPUT = _sequencer_alsa.SND_SEQ_REMOVE_INPUT
SND_SEQ_REMOVE_OUTPUT = _sequencer_alsa.SND_SEQ_REMOVE_OUTPUT
SND_SEQ_REMOVE_DEST = _sequencer_alsa.SND_SEQ_REMOVE_DEST
SND_SEQ_REMOVE_DEST_CHANNEL = _sequencer_alsa.SND_SEQ_REMOVE_DEST_CHANNEL
SND_SEQ_REMOVE_TIME_BEFORE = _sequencer_alsa.SND_SEQ_REMOVE_TIME_BEFORE
SND_SEQ_REMOVE_TIME_AFTER = _sequencer_alsa.SND_SEQ_REMOVE_TIME_AFTER
SND_SEQ_REMOVE_TIME_TICK = _sequencer_alsa.SND_SEQ_REMOVE_TIME_TICK
SND_SEQ_REMOVE_EVENT_TYPE = _sequencer_alsa.SND_SEQ_REMOVE_EVENT_TYPE
SND_SEQ_REMOVE_IGNORE_OFF = _sequencer_alsa.SND_SEQ_REMOVE_IGNORE_OFF
SND_SEQ_REMOVE_TAG_MATCH = _sequencer_alsa.SND_SEQ_REMOVE_TAG_MATCH
snd_seq_remove_events_sizeof = _sequencer_alsa.snd_seq_remove_events_sizeof
snd_seq_remove_events_malloc = _sequencer_alsa.snd_seq_remove_events_malloc
snd_seq_remove_events_free = _sequencer_alsa.snd_seq_remove_events_free
snd_seq_remove_events_copy = _sequencer_alsa.snd_seq_remove_events_copy
snd_seq_remove_events_get_condition = _sequencer_alsa.snd_seq_remove_events_get_condition
snd_seq_remove_events_get_queue = _sequencer_alsa.snd_seq_remove_events_get_queue
snd_seq_remove_events_get_time = _sequencer_alsa.snd_seq_remove_events_get_time
snd_seq_remove_events_get_dest = _sequencer_alsa.snd_seq_remove_events_get_dest
snd_seq_remove_events_get_channel = _sequencer_alsa.snd_seq_remove_events_get_channel
snd_seq_remove_events_get_event_type = _sequencer_alsa.snd_seq_remove_events_get_event_type
snd_seq_remove_events_get_tag = _sequencer_alsa.snd_seq_remove_events_get_tag
snd_seq_remove_events_set_condition = _sequencer_alsa.snd_seq_remove_events_set_condition
snd_seq_remove_events_set_queue = _sequencer_alsa.snd_seq_remove_events_set_queue
snd_seq_remove_events_set_time = _sequencer_alsa.snd_seq_remove_events_set_time
snd_seq_remove_events_set_dest = _sequencer_alsa.snd_seq_remove_events_set_dest
snd_seq_remove_events_set_channel = _sequencer_alsa.snd_seq_remove_events_set_channel
snd_seq_remove_events_set_event_type = _sequencer_alsa.snd_seq_remove_events_set_event_type
snd_seq_remove_events_set_tag = _sequencer_alsa.snd_seq_remove_events_set_tag
snd_seq_remove_events = _sequencer_alsa.snd_seq_remove_events
snd_seq_set_bit = _sequencer_alsa.snd_seq_set_bit
snd_seq_change_bit = _sequencer_alsa.snd_seq_change_bit
snd_seq_get_bit = _sequencer_alsa.snd_seq_get_bit
SND_SEQ_EVFLG_RESULT = _sequencer_alsa.SND_SEQ_EVFLG_RESULT
SND_SEQ_EVFLG_NOTE = _sequencer_alsa.SND_SEQ_EVFLG_NOTE
SND_SEQ_EVFLG_CONTROL = _sequencer_alsa.SND_SEQ_EVFLG_CONTROL
SND_SEQ_EVFLG_QUEUE = _sequencer_alsa.SND_SEQ_EVFLG_QUEUE
SND_SEQ_EVFLG_SYSTEM = _sequencer_alsa.SND_SEQ_EVFLG_SYSTEM
SND_SEQ_EVFLG_MESSAGE = _sequencer_alsa.SND_SEQ_EVFLG_MESSAGE
SND_SEQ_EVFLG_CONNECTION = _sequencer_alsa.SND_SEQ_EVFLG_CONNECTION
SND_SEQ_EVFLG_SAMPLE = _sequencer_alsa.SND_SEQ_EVFLG_SAMPLE
SND_SEQ_EVFLG_USERS = _sequencer_alsa.SND_SEQ_EVFLG_USERS
SND_SEQ_EVFLG_INSTR = _sequencer_alsa.SND_SEQ_EVFLG_INSTR
SND_SEQ_EVFLG_QUOTE = _sequencer_alsa.SND_SEQ_EVFLG_QUOTE
SND_SEQ_EVFLG_NONE = _sequencer_alsa.SND_SEQ_EVFLG_NONE
SND_SEQ_EVFLG_RAW = _sequencer_alsa.SND_SEQ_EVFLG_RAW
SND_SEQ_EVFLG_FIXED = _sequencer_alsa.SND_SEQ_EVFLG_FIXED
SND_SEQ_EVFLG_VARIABLE = _sequencer_alsa.SND_SEQ_EVFLG_VARIABLE
SND_SEQ_EVFLG_VARUSR = _sequencer_alsa.SND_SEQ_EVFLG_VARUSR
SND_SEQ_EVFLG_NOTE_ONEARG = _sequencer_alsa.SND_SEQ_EVFLG_NOTE_ONEARG
SND_SEQ_EVFLG_NOTE_TWOARG = _sequencer_alsa.SND_SEQ_EVFLG_NOTE_TWOARG
SND_SEQ_EVFLG_QUEUE_NOARG = _sequencer_alsa.SND_SEQ_EVFLG_QUEUE_NOARG
SND_SEQ_EVFLG_QUEUE_TICK = _sequencer_alsa.SND_SEQ_EVFLG_QUEUE_TICK
SND_SEQ_EVFLG_QUEUE_TIME = _sequencer_alsa.SND_SEQ_EVFLG_QUEUE_TIME
SND_SEQ_EVFLG_QUEUE_VALUE = _sequencer_alsa.SND_SEQ_EVFLG_QUEUE_VALUE
snd_seq_control_queue = _sequencer_alsa.snd_seq_control_queue
snd_seq_create_simple_port = _sequencer_alsa.snd_seq_create_simple_port
snd_seq_delete_simple_port = _sequencer_alsa.snd_seq_delete_simple_port
snd_seq_connect_from = _sequencer_alsa.snd_seq_connect_from
snd_seq_connect_to = _sequencer_alsa.snd_seq_connect_to
snd_seq_disconnect_from = _sequencer_alsa.snd_seq_disconnect_from
snd_seq_disconnect_to = _sequencer_alsa.snd_seq_disconnect_to
snd_seq_set_client_name = _sequencer_alsa.snd_seq_set_client_name
snd_seq_set_client_event_filter = _sequencer_alsa.snd_seq_set_client_event_filter
snd_seq_set_client_pool_output = _sequencer_alsa.snd_seq_set_client_pool_output
snd_seq_set_client_pool_output_room = _sequencer_alsa.snd_seq_set_client_pool_output_room
snd_seq_set_client_pool_input = _sequencer_alsa.snd_seq_set_client_pool_input
snd_seq_sync_output_queue = _sequencer_alsa.snd_seq_sync_output_queue
snd_seq_parse_address = _sequencer_alsa.snd_seq_parse_address
snd_seq_reset_pool_output = _sequencer_alsa.snd_seq_reset_pool_output
snd_seq_reset_pool_input = _sequencer_alsa.snd_seq_reset_pool_input
SND_SEQ_EVENT_SYSTEM = _sequencer_alsa.SND_SEQ_EVENT_SYSTEM
SND_SEQ_EVENT_RESULT = _sequencer_alsa.SND_SEQ_EVENT_RESULT
SND_SEQ_EVENT_NOTE = _sequencer_alsa.SND_SEQ_EVENT_NOTE
SND_SEQ_EVENT_NOTEON = _sequencer_alsa.SND_SEQ_EVENT_NOTEON
SND_SEQ_EVENT_NOTEOFF = _sequencer_alsa.SND_SEQ_EVENT_NOTEOFF
SND_SEQ_EVENT_KEYPRESS = _sequencer_alsa.SND_SEQ_EVENT_KEYPRESS
SND_SEQ_EVENT_CONTROLLER = _sequencer_alsa.SND_SEQ_EVENT_CONTROLLER
SND_SEQ_EVENT_PGMCHANGE = _sequencer_alsa.SND_SEQ_EVENT_PGMCHANGE
SND_SEQ_EVENT_CHANPRESS = _sequencer_alsa.SND_SEQ_EVENT_CHANPRESS
SND_SEQ_EVENT_PITCHBEND = _sequencer_alsa.SND_SEQ_EVENT_PITCHBEND
SND_SEQ_EVENT_CONTROL14 = _sequencer_alsa.SND_SEQ_EVENT_CONTROL14
SND_SEQ_EVENT_NONREGPARAM = _sequencer_alsa.SND_SEQ_EVENT_NONREGPARAM
SND_SEQ_EVENT_REGPARAM = _sequencer_alsa.SND_SEQ_EVENT_REGPARAM
SND_SEQ_EVENT_SONGPOS = _sequencer_alsa.SND_SEQ_EVENT_SONGPOS
SND_SEQ_EVENT_SONGSEL = _sequencer_alsa.SND_SEQ_EVENT_SONGSEL
SND_SEQ_EVENT_QFRAME = _sequencer_alsa.SND_SEQ_EVENT_QFRAME
SND_SEQ_EVENT_TIMESIGN = _sequencer_alsa.SND_SEQ_EVENT_TIMESIGN
SND_SEQ_EVENT_KEYSIGN = _sequencer_alsa.SND_SEQ_EVENT_KEYSIGN
SND_SEQ_EVENT_START = _sequencer_alsa.SND_SEQ_EVENT_START
SND_SEQ_EVENT_CONTINUE = _sequencer_alsa.SND_SEQ_EVENT_CONTINUE
SND_SEQ_EVENT_STOP = _sequencer_alsa.SND_SEQ_EVENT_STOP
SND_SEQ_EVENT_SETPOS_TICK = _sequencer_alsa.SND_SEQ_EVENT_SETPOS_TICK
SND_SEQ_EVENT_SETPOS_TIME = _sequencer_alsa.SND_SEQ_EVENT_SETPOS_TIME
SND_SEQ_EVENT_TEMPO = _sequencer_alsa.SND_SEQ_EVENT_TEMPO
SND_SEQ_EVENT_CLOCK = _sequencer_alsa.SND_SEQ_EVENT_CLOCK
SND_SEQ_EVENT_TICK = _sequencer_alsa.SND_SEQ_EVENT_TICK
SND_SEQ_EVENT_QUEUE_SKEW = _sequencer_alsa.SND_SEQ_EVENT_QUEUE_SKEW
SND_SEQ_EVENT_SYNC_POS = _sequencer_alsa.SND_SEQ_EVENT_SYNC_POS
SND_SEQ_EVENT_TUNE_REQUEST = _sequencer_alsa.SND_SEQ_EVENT_TUNE_REQUEST
SND_SEQ_EVENT_RESET = _sequencer_alsa.SND_SEQ_EVENT_RESET
SND_SEQ_EVENT_SENSING = _sequencer_alsa.SND_SEQ_EVENT_SENSING
SND_SEQ_EVENT_ECHO = _sequencer_alsa.SND_SEQ_EVENT_ECHO
SND_SEQ_EVENT_OSS = _sequencer_alsa.SND_SEQ_EVENT_OSS
SND_SEQ_EVENT_CLIENT_START = _sequencer_alsa.SND_SEQ_EVENT_CLIENT_START
SND_SEQ_EVENT_CLIENT_EXIT = _sequencer_alsa.SND_SEQ_EVENT_CLIENT_EXIT
SND_SEQ_EVENT_CLIENT_CHANGE = _sequencer_alsa.SND_SEQ_EVENT_CLIENT_CHANGE
SND_SEQ_EVENT_PORT_START = _sequencer_alsa.SND_SEQ_EVENT_PORT_START
SND_SEQ_EVENT_PORT_EXIT = _sequencer_alsa.SND_SEQ_EVENT_PORT_EXIT
SND_SEQ_EVENT_PORT_CHANGE = _sequencer_alsa.SND_SEQ_EVENT_PORT_CHANGE
SND_SEQ_EVENT_PORT_SUBSCRIBED = _sequencer_alsa.SND_SEQ_EVENT_PORT_SUBSCRIBED
SND_SEQ_EVENT_PORT_UNSUBSCRIBED = _sequencer_alsa.SND_SEQ_EVENT_PORT_UNSUBSCRIBED
SND_SEQ_EVENT_SAMPLE = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE
SND_SEQ_EVENT_SAMPLE_CLUSTER = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_CLUSTER
SND_SEQ_EVENT_SAMPLE_START = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_START
SND_SEQ_EVENT_SAMPLE_STOP = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_STOP
SND_SEQ_EVENT_SAMPLE_FREQ = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_FREQ
SND_SEQ_EVENT_SAMPLE_VOLUME = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_VOLUME
SND_SEQ_EVENT_SAMPLE_LOOP = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_LOOP
SND_SEQ_EVENT_SAMPLE_POSITION = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_POSITION
SND_SEQ_EVENT_SAMPLE_PRIVATE1 = _sequencer_alsa.SND_SEQ_EVENT_SAMPLE_PRIVATE1
SND_SEQ_EVENT_USR0 = _sequencer_alsa.SND_SEQ_EVENT_USR0
SND_SEQ_EVENT_USR1 = _sequencer_alsa.SND_SEQ_EVENT_USR1
SND_SEQ_EVENT_USR2 = _sequencer_alsa.SND_SEQ_EVENT_USR2
SND_SEQ_EVENT_USR3 = _sequencer_alsa.SND_SEQ_EVENT_USR3
SND_SEQ_EVENT_USR4 = _sequencer_alsa.SND_SEQ_EVENT_USR4
SND_SEQ_EVENT_USR5 = _sequencer_alsa.SND_SEQ_EVENT_USR5
SND_SEQ_EVENT_USR6 = _sequencer_alsa.SND_SEQ_EVENT_USR6
SND_SEQ_EVENT_USR7 = _sequencer_alsa.SND_SEQ_EVENT_USR7
SND_SEQ_EVENT_USR8 = _sequencer_alsa.SND_SEQ_EVENT_USR8
SND_SEQ_EVENT_USR9 = _sequencer_alsa.SND_SEQ_EVENT_USR9
SND_SEQ_EVENT_INSTR_BEGIN = _sequencer_alsa.SND_SEQ_EVENT_INSTR_BEGIN
SND_SEQ_EVENT_INSTR_END = _sequencer_alsa.SND_SEQ_EVENT_INSTR_END
SND_SEQ_EVENT_INSTR_INFO = _sequencer_alsa.SND_SEQ_EVENT_INSTR_INFO
SND_SEQ_EVENT_INSTR_INFO_RESULT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_INFO_RESULT
SND_SEQ_EVENT_INSTR_FINFO = _sequencer_alsa.SND_SEQ_EVENT_INSTR_FINFO
SND_SEQ_EVENT_INSTR_FINFO_RESULT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_FINFO_RESULT
SND_SEQ_EVENT_INSTR_RESET = _sequencer_alsa.SND_SEQ_EVENT_INSTR_RESET
SND_SEQ_EVENT_INSTR_STATUS = _sequencer_alsa.SND_SEQ_EVENT_INSTR_STATUS
SND_SEQ_EVENT_INSTR_STATUS_RESULT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_STATUS_RESULT
SND_SEQ_EVENT_INSTR_PUT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_PUT
SND_SEQ_EVENT_INSTR_GET = _sequencer_alsa.SND_SEQ_EVENT_INSTR_GET
SND_SEQ_EVENT_INSTR_GET_RESULT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_GET_RESULT
SND_SEQ_EVENT_INSTR_FREE = _sequencer_alsa.SND_SEQ_EVENT_INSTR_FREE
SND_SEQ_EVENT_INSTR_LIST = _sequencer_alsa.SND_SEQ_EVENT_INSTR_LIST
SND_SEQ_EVENT_INSTR_LIST_RESULT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_LIST_RESULT
SND_SEQ_EVENT_INSTR_CLUSTER = _sequencer_alsa.SND_SEQ_EVENT_INSTR_CLUSTER
SND_SEQ_EVENT_INSTR_CLUSTER_GET = _sequencer_alsa.SND_SEQ_EVENT_INSTR_CLUSTER_GET
SND_SEQ_EVENT_INSTR_CLUSTER_RESULT = _sequencer_alsa.SND_SEQ_EVENT_INSTR_CLUSTER_RESULT
SND_SEQ_EVENT_INSTR_CHANGE = _sequencer_alsa.SND_SEQ_EVENT_INSTR_CHANGE
SND_SEQ_EVENT_SYSEX = _sequencer_alsa.SND_SEQ_EVENT_SYSEX
SND_SEQ_EVENT_BOUNCE = _sequencer_alsa.SND_SEQ_EVENT_BOUNCE
SND_SEQ_EVENT_USR_VAR0 = _sequencer_alsa.SND_SEQ_EVENT_USR_VAR0
SND_SEQ_EVENT_USR_VAR1 = _sequencer_alsa.SND_SEQ_EVENT_USR_VAR1
SND_SEQ_EVENT_USR_VAR2 = _sequencer_alsa.SND_SEQ_EVENT_USR_VAR2
SND_SEQ_EVENT_USR_VAR3 = _sequencer_alsa.SND_SEQ_EVENT_USR_VAR3
SND_SEQ_EVENT_USR_VAR4 = _sequencer_alsa.SND_SEQ_EVENT_USR_VAR4
SND_SEQ_EVENT_NONE = _sequencer_alsa.SND_SEQ_EVENT_NONE
class snd_seq_addr_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_addr_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_addr_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["client"] = _sequencer_alsa.snd_seq_addr_t_client_set
    __swig_getmethods__["client"] = _sequencer_alsa.snd_seq_addr_t_client_get
    if _newclass:client = property(_sequencer_alsa.snd_seq_addr_t_client_get, _sequencer_alsa.snd_seq_addr_t_client_set)
    __swig_setmethods__["port"] = _sequencer_alsa.snd_seq_addr_t_port_set
    __swig_getmethods__["port"] = _sequencer_alsa.snd_seq_addr_t_port_get
    if _newclass:port = property(_sequencer_alsa.snd_seq_addr_t_port_get, _sequencer_alsa.snd_seq_addr_t_port_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_addr_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_addr_t
    __del__ = lambda self : None;
snd_seq_addr_t_swigregister = _sequencer_alsa.snd_seq_addr_t_swigregister
snd_seq_addr_t_swigregister(snd_seq_addr_t)
cvar = _sequencer_alsa.cvar
snd_seq_event_types = cvar.snd_seq_event_types

class snd_seq_connect_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_connect_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_connect_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sender"] = _sequencer_alsa.snd_seq_connect_t_sender_set
    __swig_getmethods__["sender"] = _sequencer_alsa.snd_seq_connect_t_sender_get
    if _newclass:sender = property(_sequencer_alsa.snd_seq_connect_t_sender_get, _sequencer_alsa.snd_seq_connect_t_sender_set)
    __swig_setmethods__["dest"] = _sequencer_alsa.snd_seq_connect_t_dest_set
    __swig_getmethods__["dest"] = _sequencer_alsa.snd_seq_connect_t_dest_get
    if _newclass:dest = property(_sequencer_alsa.snd_seq_connect_t_dest_get, _sequencer_alsa.snd_seq_connect_t_dest_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_connect_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_connect_t
    __del__ = lambda self : None;
snd_seq_connect_t_swigregister = _sequencer_alsa.snd_seq_connect_t_swigregister
snd_seq_connect_t_swigregister(snd_seq_connect_t)

class snd_seq_real_time_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_real_time_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_real_time_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tv_sec"] = _sequencer_alsa.snd_seq_real_time_t_tv_sec_set
    __swig_getmethods__["tv_sec"] = _sequencer_alsa.snd_seq_real_time_t_tv_sec_get
    if _newclass:tv_sec = property(_sequencer_alsa.snd_seq_real_time_t_tv_sec_get, _sequencer_alsa.snd_seq_real_time_t_tv_sec_set)
    __swig_setmethods__["tv_nsec"] = _sequencer_alsa.snd_seq_real_time_t_tv_nsec_set
    __swig_getmethods__["tv_nsec"] = _sequencer_alsa.snd_seq_real_time_t_tv_nsec_get
    if _newclass:tv_nsec = property(_sequencer_alsa.snd_seq_real_time_t_tv_nsec_get, _sequencer_alsa.snd_seq_real_time_t_tv_nsec_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_real_time_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_real_time_t
    __del__ = lambda self : None;
snd_seq_real_time_t_swigregister = _sequencer_alsa.snd_seq_real_time_t_swigregister
snd_seq_real_time_t_swigregister(snd_seq_real_time_t)

class snd_seq_timestamp_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_timestamp_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_timestamp_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["tick"] = _sequencer_alsa.snd_seq_timestamp_t_tick_set
    __swig_getmethods__["tick"] = _sequencer_alsa.snd_seq_timestamp_t_tick_get
    if _newclass:tick = property(_sequencer_alsa.snd_seq_timestamp_t_tick_get, _sequencer_alsa.snd_seq_timestamp_t_tick_set)
    __swig_setmethods__["time"] = _sequencer_alsa.snd_seq_timestamp_t_time_set
    __swig_getmethods__["time"] = _sequencer_alsa.snd_seq_timestamp_t_time_get
    if _newclass:time = property(_sequencer_alsa.snd_seq_timestamp_t_time_get, _sequencer_alsa.snd_seq_timestamp_t_time_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_timestamp_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_timestamp_t
    __del__ = lambda self : None;
snd_seq_timestamp_t_swigregister = _sequencer_alsa.snd_seq_timestamp_t_swigregister
snd_seq_timestamp_t_swigregister(snd_seq_timestamp_t)

SND_SEQ_TIME_STAMP_TICK = _sequencer_alsa.SND_SEQ_TIME_STAMP_TICK
SND_SEQ_TIME_STAMP_REAL = _sequencer_alsa.SND_SEQ_TIME_STAMP_REAL
SND_SEQ_TIME_STAMP_MASK = _sequencer_alsa.SND_SEQ_TIME_STAMP_MASK
SND_SEQ_TIME_MODE_ABS = _sequencer_alsa.SND_SEQ_TIME_MODE_ABS
SND_SEQ_TIME_MODE_REL = _sequencer_alsa.SND_SEQ_TIME_MODE_REL
SND_SEQ_TIME_MODE_MASK = _sequencer_alsa.SND_SEQ_TIME_MODE_MASK
SND_SEQ_EVENT_LENGTH_FIXED = _sequencer_alsa.SND_SEQ_EVENT_LENGTH_FIXED
SND_SEQ_EVENT_LENGTH_VARIABLE = _sequencer_alsa.SND_SEQ_EVENT_LENGTH_VARIABLE
SND_SEQ_EVENT_LENGTH_VARUSR = _sequencer_alsa.SND_SEQ_EVENT_LENGTH_VARUSR
SND_SEQ_EVENT_LENGTH_MASK = _sequencer_alsa.SND_SEQ_EVENT_LENGTH_MASK
SND_SEQ_PRIORITY_NORMAL = _sequencer_alsa.SND_SEQ_PRIORITY_NORMAL
SND_SEQ_PRIORITY_HIGH = _sequencer_alsa.SND_SEQ_PRIORITY_HIGH
SND_SEQ_PRIORITY_MASK = _sequencer_alsa.SND_SEQ_PRIORITY_MASK
class snd_seq_ev_note_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_note_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_note_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["channel"] = _sequencer_alsa.snd_seq_ev_note_t_channel_set
    __swig_getmethods__["channel"] = _sequencer_alsa.snd_seq_ev_note_t_channel_get
    if _newclass:channel = property(_sequencer_alsa.snd_seq_ev_note_t_channel_get, _sequencer_alsa.snd_seq_ev_note_t_channel_set)
    __swig_setmethods__["note"] = _sequencer_alsa.snd_seq_ev_note_t_note_set
    __swig_getmethods__["note"] = _sequencer_alsa.snd_seq_ev_note_t_note_get
    if _newclass:note = property(_sequencer_alsa.snd_seq_ev_note_t_note_get, _sequencer_alsa.snd_seq_ev_note_t_note_set)
    __swig_setmethods__["velocity"] = _sequencer_alsa.snd_seq_ev_note_t_velocity_set
    __swig_getmethods__["velocity"] = _sequencer_alsa.snd_seq_ev_note_t_velocity_get
    if _newclass:velocity = property(_sequencer_alsa.snd_seq_ev_note_t_velocity_get, _sequencer_alsa.snd_seq_ev_note_t_velocity_set)
    __swig_setmethods__["off_velocity"] = _sequencer_alsa.snd_seq_ev_note_t_off_velocity_set
    __swig_getmethods__["off_velocity"] = _sequencer_alsa.snd_seq_ev_note_t_off_velocity_get
    if _newclass:off_velocity = property(_sequencer_alsa.snd_seq_ev_note_t_off_velocity_get, _sequencer_alsa.snd_seq_ev_note_t_off_velocity_set)
    __swig_setmethods__["duration"] = _sequencer_alsa.snd_seq_ev_note_t_duration_set
    __swig_getmethods__["duration"] = _sequencer_alsa.snd_seq_ev_note_t_duration_get
    if _newclass:duration = property(_sequencer_alsa.snd_seq_ev_note_t_duration_get, _sequencer_alsa.snd_seq_ev_note_t_duration_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_note_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_note_t
    __del__ = lambda self : None;
snd_seq_ev_note_t_swigregister = _sequencer_alsa.snd_seq_ev_note_t_swigregister
snd_seq_ev_note_t_swigregister(snd_seq_ev_note_t)

class snd_seq_ev_ctrl_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_ctrl_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_ctrl_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["channel"] = _sequencer_alsa.snd_seq_ev_ctrl_t_channel_set
    __swig_getmethods__["channel"] = _sequencer_alsa.snd_seq_ev_ctrl_t_channel_get
    if _newclass:channel = property(_sequencer_alsa.snd_seq_ev_ctrl_t_channel_get, _sequencer_alsa.snd_seq_ev_ctrl_t_channel_set)
    __swig_setmethods__["unused"] = _sequencer_alsa.snd_seq_ev_ctrl_t_unused_set
    __swig_getmethods__["unused"] = _sequencer_alsa.snd_seq_ev_ctrl_t_unused_get
    if _newclass:unused = property(_sequencer_alsa.snd_seq_ev_ctrl_t_unused_get, _sequencer_alsa.snd_seq_ev_ctrl_t_unused_set)
    __swig_setmethods__["param"] = _sequencer_alsa.snd_seq_ev_ctrl_t_param_set
    __swig_getmethods__["param"] = _sequencer_alsa.snd_seq_ev_ctrl_t_param_get
    if _newclass:param = property(_sequencer_alsa.snd_seq_ev_ctrl_t_param_get, _sequencer_alsa.snd_seq_ev_ctrl_t_param_set)
    __swig_setmethods__["value"] = _sequencer_alsa.snd_seq_ev_ctrl_t_value_set
    __swig_getmethods__["value"] = _sequencer_alsa.snd_seq_ev_ctrl_t_value_get
    if _newclass:value = property(_sequencer_alsa.snd_seq_ev_ctrl_t_value_get, _sequencer_alsa.snd_seq_ev_ctrl_t_value_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_ctrl_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_ctrl_t
    __del__ = lambda self : None;
snd_seq_ev_ctrl_t_swigregister = _sequencer_alsa.snd_seq_ev_ctrl_t_swigregister
snd_seq_ev_ctrl_t_swigregister(snd_seq_ev_ctrl_t)

class snd_seq_ev_raw8_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_raw8_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_raw8_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["d"] = _sequencer_alsa.snd_seq_ev_raw8_t_d_set
    __swig_getmethods__["d"] = _sequencer_alsa.snd_seq_ev_raw8_t_d_get
    if _newclass:d = property(_sequencer_alsa.snd_seq_ev_raw8_t_d_get, _sequencer_alsa.snd_seq_ev_raw8_t_d_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_raw8_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_raw8_t
    __del__ = lambda self : None;
snd_seq_ev_raw8_t_swigregister = _sequencer_alsa.snd_seq_ev_raw8_t_swigregister
snd_seq_ev_raw8_t_swigregister(snd_seq_ev_raw8_t)

class snd_seq_ev_raw32_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_raw32_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_raw32_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["d"] = _sequencer_alsa.snd_seq_ev_raw32_t_d_set
    __swig_getmethods__["d"] = _sequencer_alsa.snd_seq_ev_raw32_t_d_get
    if _newclass:d = property(_sequencer_alsa.snd_seq_ev_raw32_t_d_get, _sequencer_alsa.snd_seq_ev_raw32_t_d_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_raw32_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_raw32_t
    __del__ = lambda self : None;
snd_seq_ev_raw32_t_swigregister = _sequencer_alsa.snd_seq_ev_raw32_t_swigregister
snd_seq_ev_raw32_t_swigregister(snd_seq_ev_raw32_t)

class snd_seq_ev_ext_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_ext_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_ext_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["len"] = _sequencer_alsa.snd_seq_ev_ext_t_len_set
    __swig_getmethods__["len"] = _sequencer_alsa.snd_seq_ev_ext_t_len_get
    if _newclass:len = property(_sequencer_alsa.snd_seq_ev_ext_t_len_get, _sequencer_alsa.snd_seq_ev_ext_t_len_set)
    __swig_setmethods__["ptr"] = _sequencer_alsa.snd_seq_ev_ext_t_ptr_set
    __swig_getmethods__["ptr"] = _sequencer_alsa.snd_seq_ev_ext_t_ptr_get
    if _newclass:ptr = property(_sequencer_alsa.snd_seq_ev_ext_t_ptr_get, _sequencer_alsa.snd_seq_ev_ext_t_ptr_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_ext_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_ext_t
    __del__ = lambda self : None;
snd_seq_ev_ext_t_swigregister = _sequencer_alsa.snd_seq_ev_ext_t_swigregister
snd_seq_ev_ext_t_swigregister(snd_seq_ev_ext_t)

class snd_seq_instr_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_instr_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_instr_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cluster"] = _sequencer_alsa.snd_seq_instr_t_cluster_set
    __swig_getmethods__["cluster"] = _sequencer_alsa.snd_seq_instr_t_cluster_get
    if _newclass:cluster = property(_sequencer_alsa.snd_seq_instr_t_cluster_get, _sequencer_alsa.snd_seq_instr_t_cluster_set)
    __swig_setmethods__["std"] = _sequencer_alsa.snd_seq_instr_t_std_set
    __swig_getmethods__["std"] = _sequencer_alsa.snd_seq_instr_t_std_get
    if _newclass:std = property(_sequencer_alsa.snd_seq_instr_t_std_get, _sequencer_alsa.snd_seq_instr_t_std_set)
    __swig_setmethods__["bank"] = _sequencer_alsa.snd_seq_instr_t_bank_set
    __swig_getmethods__["bank"] = _sequencer_alsa.snd_seq_instr_t_bank_get
    if _newclass:bank = property(_sequencer_alsa.snd_seq_instr_t_bank_get, _sequencer_alsa.snd_seq_instr_t_bank_set)
    __swig_setmethods__["prg"] = _sequencer_alsa.snd_seq_instr_t_prg_set
    __swig_getmethods__["prg"] = _sequencer_alsa.snd_seq_instr_t_prg_get
    if _newclass:prg = property(_sequencer_alsa.snd_seq_instr_t_prg_get, _sequencer_alsa.snd_seq_instr_t_prg_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_instr_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_instr_t
    __del__ = lambda self : None;
snd_seq_instr_t_swigregister = _sequencer_alsa.snd_seq_instr_t_swigregister
snd_seq_instr_t_swigregister(snd_seq_instr_t)

class snd_seq_ev_sample_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_sample_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_sample_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["std"] = _sequencer_alsa.snd_seq_ev_sample_t_std_set
    __swig_getmethods__["std"] = _sequencer_alsa.snd_seq_ev_sample_t_std_get
    if _newclass:std = property(_sequencer_alsa.snd_seq_ev_sample_t_std_get, _sequencer_alsa.snd_seq_ev_sample_t_std_set)
    __swig_setmethods__["bank"] = _sequencer_alsa.snd_seq_ev_sample_t_bank_set
    __swig_getmethods__["bank"] = _sequencer_alsa.snd_seq_ev_sample_t_bank_get
    if _newclass:bank = property(_sequencer_alsa.snd_seq_ev_sample_t_bank_get, _sequencer_alsa.snd_seq_ev_sample_t_bank_set)
    __swig_setmethods__["prg"] = _sequencer_alsa.snd_seq_ev_sample_t_prg_set
    __swig_getmethods__["prg"] = _sequencer_alsa.snd_seq_ev_sample_t_prg_get
    if _newclass:prg = property(_sequencer_alsa.snd_seq_ev_sample_t_prg_get, _sequencer_alsa.snd_seq_ev_sample_t_prg_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_sample_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_sample_t
    __del__ = lambda self : None;
snd_seq_ev_sample_t_swigregister = _sequencer_alsa.snd_seq_ev_sample_t_swigregister
snd_seq_ev_sample_t_swigregister(snd_seq_ev_sample_t)

class snd_seq_ev_cluster_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_cluster_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_cluster_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["cluster"] = _sequencer_alsa.snd_seq_ev_cluster_t_cluster_set
    __swig_getmethods__["cluster"] = _sequencer_alsa.snd_seq_ev_cluster_t_cluster_get
    if _newclass:cluster = property(_sequencer_alsa.snd_seq_ev_cluster_t_cluster_get, _sequencer_alsa.snd_seq_ev_cluster_t_cluster_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_cluster_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_cluster_t
    __del__ = lambda self : None;
snd_seq_ev_cluster_t_swigregister = _sequencer_alsa.snd_seq_ev_cluster_t_swigregister
snd_seq_ev_cluster_t_swigregister(snd_seq_ev_cluster_t)

SND_SEQ_SAMPLE_STOP_IMMEDIATELY = _sequencer_alsa.SND_SEQ_SAMPLE_STOP_IMMEDIATELY
SND_SEQ_SAMPLE_STOP_VENVELOPE = _sequencer_alsa.SND_SEQ_SAMPLE_STOP_VENVELOPE
SND_SEQ_SAMPLE_STOP_LOOP = _sequencer_alsa.SND_SEQ_SAMPLE_STOP_LOOP
class snd_seq_ev_volume_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_volume_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_volume_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["volume"] = _sequencer_alsa.snd_seq_ev_volume_t_volume_set
    __swig_getmethods__["volume"] = _sequencer_alsa.snd_seq_ev_volume_t_volume_get
    if _newclass:volume = property(_sequencer_alsa.snd_seq_ev_volume_t_volume_get, _sequencer_alsa.snd_seq_ev_volume_t_volume_set)
    __swig_setmethods__["lr"] = _sequencer_alsa.snd_seq_ev_volume_t_lr_set
    __swig_getmethods__["lr"] = _sequencer_alsa.snd_seq_ev_volume_t_lr_get
    if _newclass:lr = property(_sequencer_alsa.snd_seq_ev_volume_t_lr_get, _sequencer_alsa.snd_seq_ev_volume_t_lr_set)
    __swig_setmethods__["fr"] = _sequencer_alsa.snd_seq_ev_volume_t_fr_set
    __swig_getmethods__["fr"] = _sequencer_alsa.snd_seq_ev_volume_t_fr_get
    if _newclass:fr = property(_sequencer_alsa.snd_seq_ev_volume_t_fr_get, _sequencer_alsa.snd_seq_ev_volume_t_fr_set)
    __swig_setmethods__["du"] = _sequencer_alsa.snd_seq_ev_volume_t_du_set
    __swig_getmethods__["du"] = _sequencer_alsa.snd_seq_ev_volume_t_du_get
    if _newclass:du = property(_sequencer_alsa.snd_seq_ev_volume_t_du_get, _sequencer_alsa.snd_seq_ev_volume_t_du_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_volume_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_volume_t
    __del__ = lambda self : None;
snd_seq_ev_volume_t_swigregister = _sequencer_alsa.snd_seq_ev_volume_t_swigregister
snd_seq_ev_volume_t_swigregister(snd_seq_ev_volume_t)

class snd_seq_ev_loop_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_loop_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_loop_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["start"] = _sequencer_alsa.snd_seq_ev_loop_t_start_set
    __swig_getmethods__["start"] = _sequencer_alsa.snd_seq_ev_loop_t_start_get
    if _newclass:start = property(_sequencer_alsa.snd_seq_ev_loop_t_start_get, _sequencer_alsa.snd_seq_ev_loop_t_start_set)
    __swig_setmethods__["end"] = _sequencer_alsa.snd_seq_ev_loop_t_end_set
    __swig_getmethods__["end"] = _sequencer_alsa.snd_seq_ev_loop_t_end_get
    if _newclass:end = property(_sequencer_alsa.snd_seq_ev_loop_t_end_get, _sequencer_alsa.snd_seq_ev_loop_t_end_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_loop_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_loop_t
    __del__ = lambda self : None;
snd_seq_ev_loop_t_swigregister = _sequencer_alsa.snd_seq_ev_loop_t_swigregister
snd_seq_ev_loop_t_swigregister(snd_seq_ev_loop_t)

class snd_seq_ev_sample_control_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_sample_control_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_sample_control_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["channel"] = _sequencer_alsa.snd_seq_ev_sample_control_t_channel_set
    __swig_getmethods__["channel"] = _sequencer_alsa.snd_seq_ev_sample_control_t_channel_get
    if _newclass:channel = property(_sequencer_alsa.snd_seq_ev_sample_control_t_channel_get, _sequencer_alsa.snd_seq_ev_sample_control_t_channel_set)
    __swig_setmethods__["unused"] = _sequencer_alsa.snd_seq_ev_sample_control_t_unused_set
    __swig_getmethods__["unused"] = _sequencer_alsa.snd_seq_ev_sample_control_t_unused_get
    if _newclass:unused = property(_sequencer_alsa.snd_seq_ev_sample_control_t_unused_get, _sequencer_alsa.snd_seq_ev_sample_control_t_unused_set)
    __swig_getmethods__["param"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_get
    if _newclass:param = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_get)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_sample_control_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_sample_control_t
    __del__ = lambda self : None;
snd_seq_ev_sample_control_t_swigregister = _sequencer_alsa.snd_seq_ev_sample_control_t_swigregister
snd_seq_ev_sample_control_t_swigregister(snd_seq_ev_sample_control_t)

class snd_seq_ev_sample_control_t_param(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_sample_control_t_param, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_sample_control_t_param, name)
    __repr__ = _swig_repr
    __swig_setmethods__["sample"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_sample_set
    __swig_getmethods__["sample"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_sample_get
    if _newclass:sample = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_sample_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_sample_set)
    __swig_setmethods__["cluster"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_cluster_set
    __swig_getmethods__["cluster"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_cluster_get
    if _newclass:cluster = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_cluster_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_cluster_set)
    __swig_setmethods__["position"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_position_set
    __swig_getmethods__["position"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_position_get
    if _newclass:position = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_position_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_position_set)
    __swig_setmethods__["stop_mode"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_stop_mode_set
    __swig_getmethods__["stop_mode"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_stop_mode_get
    if _newclass:stop_mode = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_stop_mode_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_stop_mode_set)
    __swig_setmethods__["frequency"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_frequency_set
    __swig_getmethods__["frequency"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_frequency_get
    if _newclass:frequency = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_frequency_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_frequency_set)
    __swig_setmethods__["volume"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_volume_set
    __swig_getmethods__["volume"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_volume_get
    if _newclass:volume = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_volume_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_volume_set)
    __swig_setmethods__["loop"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_loop_set
    __swig_getmethods__["loop"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_loop_get
    if _newclass:loop = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_loop_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_loop_set)
    __swig_setmethods__["raw8"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_raw8_set
    __swig_getmethods__["raw8"] = _sequencer_alsa.snd_seq_ev_sample_control_t_param_raw8_get
    if _newclass:raw8 = property(_sequencer_alsa.snd_seq_ev_sample_control_t_param_raw8_get, _sequencer_alsa.snd_seq_ev_sample_control_t_param_raw8_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_sample_control_t_param(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_sample_control_t_param
    __del__ = lambda self : None;
snd_seq_ev_sample_control_t_param_swigregister = _sequencer_alsa.snd_seq_ev_sample_control_t_param_swigregister
snd_seq_ev_sample_control_t_param_swigregister(snd_seq_ev_sample_control_t_param)

class snd_seq_ev_instr_begin_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_instr_begin_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_instr_begin_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["timeout"] = _sequencer_alsa.snd_seq_ev_instr_begin_t_timeout_set
    __swig_getmethods__["timeout"] = _sequencer_alsa.snd_seq_ev_instr_begin_t_timeout_get
    if _newclass:timeout = property(_sequencer_alsa.snd_seq_ev_instr_begin_t_timeout_get, _sequencer_alsa.snd_seq_ev_instr_begin_t_timeout_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_instr_begin_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_instr_begin_t
    __del__ = lambda self : None;
snd_seq_ev_instr_begin_t_swigregister = _sequencer_alsa.snd_seq_ev_instr_begin_t_swigregister
snd_seq_ev_instr_begin_t_swigregister(snd_seq_ev_instr_begin_t)

class snd_seq_result_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_result_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_result_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["event"] = _sequencer_alsa.snd_seq_result_t_event_set
    __swig_getmethods__["event"] = _sequencer_alsa.snd_seq_result_t_event_get
    if _newclass:event = property(_sequencer_alsa.snd_seq_result_t_event_get, _sequencer_alsa.snd_seq_result_t_event_set)
    __swig_setmethods__["result"] = _sequencer_alsa.snd_seq_result_t_result_set
    __swig_getmethods__["result"] = _sequencer_alsa.snd_seq_result_t_result_get
    if _newclass:result = property(_sequencer_alsa.snd_seq_result_t_result_get, _sequencer_alsa.snd_seq_result_t_result_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_result_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_result_t
    __del__ = lambda self : None;
snd_seq_result_t_swigregister = _sequencer_alsa.snd_seq_result_t_swigregister
snd_seq_result_t_swigregister(snd_seq_result_t)

class snd_seq_queue_skew_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_queue_skew_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_queue_skew_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _sequencer_alsa.snd_seq_queue_skew_t_value_set
    __swig_getmethods__["value"] = _sequencer_alsa.snd_seq_queue_skew_t_value_get
    if _newclass:value = property(_sequencer_alsa.snd_seq_queue_skew_t_value_get, _sequencer_alsa.snd_seq_queue_skew_t_value_set)
    __swig_setmethods__["base"] = _sequencer_alsa.snd_seq_queue_skew_t_base_set
    __swig_getmethods__["base"] = _sequencer_alsa.snd_seq_queue_skew_t_base_get
    if _newclass:base = property(_sequencer_alsa.snd_seq_queue_skew_t_base_get, _sequencer_alsa.snd_seq_queue_skew_t_base_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_queue_skew_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_queue_skew_t
    __del__ = lambda self : None;
snd_seq_queue_skew_t_swigregister = _sequencer_alsa.snd_seq_queue_skew_t_swigregister
snd_seq_queue_skew_t_swigregister(snd_seq_queue_skew_t)

class snd_seq_ev_queue_control_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_queue_control_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_queue_control_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["queue"] = _sequencer_alsa.snd_seq_ev_queue_control_t_queue_set
    __swig_getmethods__["queue"] = _sequencer_alsa.snd_seq_ev_queue_control_t_queue_get
    if _newclass:queue = property(_sequencer_alsa.snd_seq_ev_queue_control_t_queue_get, _sequencer_alsa.snd_seq_ev_queue_control_t_queue_set)
    __swig_setmethods__["unused"] = _sequencer_alsa.snd_seq_ev_queue_control_t_unused_set
    __swig_getmethods__["unused"] = _sequencer_alsa.snd_seq_ev_queue_control_t_unused_get
    if _newclass:unused = property(_sequencer_alsa.snd_seq_ev_queue_control_t_unused_get, _sequencer_alsa.snd_seq_ev_queue_control_t_unused_set)
    __swig_getmethods__["param"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_get
    if _newclass:param = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_get)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_queue_control_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_queue_control_t
    __del__ = lambda self : None;
snd_seq_ev_queue_control_t_swigregister = _sequencer_alsa.snd_seq_ev_queue_control_t_swigregister
snd_seq_ev_queue_control_t_swigregister(snd_seq_ev_queue_control_t)

class snd_seq_ev_queue_control_t_param(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_ev_queue_control_t_param, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_ev_queue_control_t_param, name)
    __repr__ = _swig_repr
    __swig_setmethods__["value"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_value_set
    __swig_getmethods__["value"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_value_get
    if _newclass:value = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_value_get, _sequencer_alsa.snd_seq_ev_queue_control_t_param_value_set)
    __swig_setmethods__["time"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_time_set
    __swig_getmethods__["time"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_time_get
    if _newclass:time = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_time_get, _sequencer_alsa.snd_seq_ev_queue_control_t_param_time_set)
    __swig_setmethods__["position"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_position_set
    __swig_getmethods__["position"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_position_get
    if _newclass:position = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_position_get, _sequencer_alsa.snd_seq_ev_queue_control_t_param_position_set)
    __swig_setmethods__["skew"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_skew_set
    __swig_getmethods__["skew"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_skew_get
    if _newclass:skew = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_skew_get, _sequencer_alsa.snd_seq_ev_queue_control_t_param_skew_set)
    __swig_setmethods__["d32"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_d32_set
    __swig_getmethods__["d32"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_d32_get
    if _newclass:d32 = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_d32_get, _sequencer_alsa.snd_seq_ev_queue_control_t_param_d32_set)
    __swig_setmethods__["d8"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_d8_set
    __swig_getmethods__["d8"] = _sequencer_alsa.snd_seq_ev_queue_control_t_param_d8_get
    if _newclass:d8 = property(_sequencer_alsa.snd_seq_ev_queue_control_t_param_d8_get, _sequencer_alsa.snd_seq_ev_queue_control_t_param_d8_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_ev_queue_control_t_param(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_ev_queue_control_t_param
    __del__ = lambda self : None;
snd_seq_ev_queue_control_t_param_swigregister = _sequencer_alsa.snd_seq_ev_queue_control_t_param_swigregister
snd_seq_ev_queue_control_t_param_swigregister(snd_seq_ev_queue_control_t_param)

class snd_seq_event_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_event_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_event_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _sequencer_alsa.snd_seq_event_t_type_set
    __swig_getmethods__["type"] = _sequencer_alsa.snd_seq_event_t_type_get
    if _newclass:type = property(_sequencer_alsa.snd_seq_event_t_type_get, _sequencer_alsa.snd_seq_event_t_type_set)
    __swig_setmethods__["flags"] = _sequencer_alsa.snd_seq_event_t_flags_set
    __swig_getmethods__["flags"] = _sequencer_alsa.snd_seq_event_t_flags_get
    if _newclass:flags = property(_sequencer_alsa.snd_seq_event_t_flags_get, _sequencer_alsa.snd_seq_event_t_flags_set)
    __swig_setmethods__["tag"] = _sequencer_alsa.snd_seq_event_t_tag_set
    __swig_getmethods__["tag"] = _sequencer_alsa.snd_seq_event_t_tag_get
    if _newclass:tag = property(_sequencer_alsa.snd_seq_event_t_tag_get, _sequencer_alsa.snd_seq_event_t_tag_set)
    __swig_setmethods__["queue"] = _sequencer_alsa.snd_seq_event_t_queue_set
    __swig_getmethods__["queue"] = _sequencer_alsa.snd_seq_event_t_queue_get
    if _newclass:queue = property(_sequencer_alsa.snd_seq_event_t_queue_get, _sequencer_alsa.snd_seq_event_t_queue_set)
    __swig_setmethods__["time"] = _sequencer_alsa.snd_seq_event_t_time_set
    __swig_getmethods__["time"] = _sequencer_alsa.snd_seq_event_t_time_get
    if _newclass:time = property(_sequencer_alsa.snd_seq_event_t_time_get, _sequencer_alsa.snd_seq_event_t_time_set)
    __swig_setmethods__["source"] = _sequencer_alsa.snd_seq_event_t_source_set
    __swig_getmethods__["source"] = _sequencer_alsa.snd_seq_event_t_source_get
    if _newclass:source = property(_sequencer_alsa.snd_seq_event_t_source_get, _sequencer_alsa.snd_seq_event_t_source_set)
    __swig_setmethods__["dest"] = _sequencer_alsa.snd_seq_event_t_dest_set
    __swig_getmethods__["dest"] = _sequencer_alsa.snd_seq_event_t_dest_get
    if _newclass:dest = property(_sequencer_alsa.snd_seq_event_t_dest_get, _sequencer_alsa.snd_seq_event_t_dest_set)
    __swig_getmethods__["data"] = _sequencer_alsa.snd_seq_event_t_data_get
    if _newclass:data = property(_sequencer_alsa.snd_seq_event_t_data_get)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_event_t(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_event_t
    __del__ = lambda self : None;
snd_seq_event_t_swigregister = _sequencer_alsa.snd_seq_event_t_swigregister
snd_seq_event_t_swigregister(snd_seq_event_t)

class snd_seq_event_t_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, snd_seq_event_t_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, snd_seq_event_t_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["note"] = _sequencer_alsa.snd_seq_event_t_data_note_set
    __swig_getmethods__["note"] = _sequencer_alsa.snd_seq_event_t_data_note_get
    if _newclass:note = property(_sequencer_alsa.snd_seq_event_t_data_note_get, _sequencer_alsa.snd_seq_event_t_data_note_set)
    __swig_setmethods__["control"] = _sequencer_alsa.snd_seq_event_t_data_control_set
    __swig_getmethods__["control"] = _sequencer_alsa.snd_seq_event_t_data_control_get
    if _newclass:control = property(_sequencer_alsa.snd_seq_event_t_data_control_get, _sequencer_alsa.snd_seq_event_t_data_control_set)
    __swig_setmethods__["raw8"] = _sequencer_alsa.snd_seq_event_t_data_raw8_set
    __swig_getmethods__["raw8"] = _sequencer_alsa.snd_seq_event_t_data_raw8_get
    if _newclass:raw8 = property(_sequencer_alsa.snd_seq_event_t_data_raw8_get, _sequencer_alsa.snd_seq_event_t_data_raw8_set)
    __swig_setmethods__["raw32"] = _sequencer_alsa.snd_seq_event_t_data_raw32_set
    __swig_getmethods__["raw32"] = _sequencer_alsa.snd_seq_event_t_data_raw32_get
    if _newclass:raw32 = property(_sequencer_alsa.snd_seq_event_t_data_raw32_get, _sequencer_alsa.snd_seq_event_t_data_raw32_set)
    __swig_setmethods__["ext"] = _sequencer_alsa.snd_seq_event_t_data_ext_set
    __swig_getmethods__["ext"] = _sequencer_alsa.snd_seq_event_t_data_ext_get
    if _newclass:ext = property(_sequencer_alsa.snd_seq_event_t_data_ext_get, _sequencer_alsa.snd_seq_event_t_data_ext_set)
    __swig_setmethods__["queue"] = _sequencer_alsa.snd_seq_event_t_data_queue_set
    __swig_getmethods__["queue"] = _sequencer_alsa.snd_seq_event_t_data_queue_get
    if _newclass:queue = property(_sequencer_alsa.snd_seq_event_t_data_queue_get, _sequencer_alsa.snd_seq_event_t_data_queue_set)
    __swig_setmethods__["time"] = _sequencer_alsa.snd_seq_event_t_data_time_set
    __swig_getmethods__["time"] = _sequencer_alsa.snd_seq_event_t_data_time_get
    if _newclass:time = property(_sequencer_alsa.snd_seq_event_t_data_time_get, _sequencer_alsa.snd_seq_event_t_data_time_set)
    __swig_setmethods__["addr"] = _sequencer_alsa.snd_seq_event_t_data_addr_set
    __swig_getmethods__["addr"] = _sequencer_alsa.snd_seq_event_t_data_addr_get
    if _newclass:addr = property(_sequencer_alsa.snd_seq_event_t_data_addr_get, _sequencer_alsa.snd_seq_event_t_data_addr_set)
    __swig_setmethods__["connect"] = _sequencer_alsa.snd_seq_event_t_data_connect_set
    __swig_getmethods__["connect"] = _sequencer_alsa.snd_seq_event_t_data_connect_get
    if _newclass:connect = property(_sequencer_alsa.snd_seq_event_t_data_connect_get, _sequencer_alsa.snd_seq_event_t_data_connect_set)
    __swig_setmethods__["result"] = _sequencer_alsa.snd_seq_event_t_data_result_set
    __swig_getmethods__["result"] = _sequencer_alsa.snd_seq_event_t_data_result_get
    if _newclass:result = property(_sequencer_alsa.snd_seq_event_t_data_result_get, _sequencer_alsa.snd_seq_event_t_data_result_set)
    __swig_setmethods__["instr_begin"] = _sequencer_alsa.snd_seq_event_t_data_instr_begin_set
    __swig_getmethods__["instr_begin"] = _sequencer_alsa.snd_seq_event_t_data_instr_begin_get
    if _newclass:instr_begin = property(_sequencer_alsa.snd_seq_event_t_data_instr_begin_get, _sequencer_alsa.snd_seq_event_t_data_instr_begin_set)
    __swig_setmethods__["sample"] = _sequencer_alsa.snd_seq_event_t_data_sample_set
    __swig_getmethods__["sample"] = _sequencer_alsa.snd_seq_event_t_data_sample_get
    if _newclass:sample = property(_sequencer_alsa.snd_seq_event_t_data_sample_get, _sequencer_alsa.snd_seq_event_t_data_sample_set)
    def __init__(self, *args):
        this = _sequencer_alsa.new_snd_seq_event_t_data(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _sequencer_alsa.delete_snd_seq_event_t_data
    __del__ = lambda self : None;
snd_seq_event_t_data_swigregister = _sequencer_alsa.snd_seq_event_t_data_swigregister
snd_seq_event_t_data_swigregister(snd_seq_event_t_data)

snd_midi_event_new = _sequencer_alsa.snd_midi_event_new
snd_midi_event_resize_buffer = _sequencer_alsa.snd_midi_event_resize_buffer
snd_midi_event_free = _sequencer_alsa.snd_midi_event_free
snd_midi_event_init = _sequencer_alsa.snd_midi_event_init
snd_midi_event_reset_encode = _sequencer_alsa.snd_midi_event_reset_encode
snd_midi_event_reset_decode = _sequencer_alsa.snd_midi_event_reset_decode
snd_midi_event_no_status = _sequencer_alsa.snd_midi_event_no_status
snd_midi_event_encode = _sequencer_alsa.snd_midi_event_encode
snd_midi_event_encode_byte = _sequencer_alsa.snd_midi_event_encode_byte
snd_midi_event_decode = _sequencer_alsa.snd_midi_event_decode
SND_ERROR_BEGIN = _sequencer_alsa.SND_ERROR_BEGIN
SND_ERROR_INCOMPATIBLE_VERSION = _sequencer_alsa.SND_ERROR_INCOMPATIBLE_VERSION
SND_ERROR_ALISP_NIL = _sequencer_alsa.SND_ERROR_ALISP_NIL
snd_strerror = _sequencer_alsa.snd_strerror
snd_lib_error_set_handler = _sequencer_alsa.snd_lib_error_set_handler


