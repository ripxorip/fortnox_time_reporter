fortnox_time_reporter_sources = [
  'main.c',
  'fortnox_time_reporter-application.c',
  'fortnox_time_reporter-window.c',
]

fortnox_time_reporter_deps = [
  dependency('gtk4'),
  dependency('libadwaita-1', version: '>= 1.2'),
]

fortnox_time_reporter_sources += gnome.compile_resources('fortnox_time_reporter-resources',
  'fortnox_time_reporter.gresource.xml',
  c_name: 'fortnox_time_reporter'
)

executable('fortnox_time_reporter', fortnox_time_reporter_sources,
  dependencies: fortnox_time_reporter_deps,
       install: true,
)
