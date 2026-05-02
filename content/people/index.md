---
title: People

type: landing

sections:
  - block: hero
    content:
      title: Current WING members
      caption: "WING with alumni @ ACL '24 (Bangkok, Thailand)"
    design:
      background:
        image: 
          filename: 'acl24-banner.jpg'
          position: center
          size: cover             # Covers entire background
          filters:
            brightness: 0.2
        text_color_light: true
      parallax: true         # Optional parallax effect

  # Current WING Block
  - block: people
    content:
      # title: Meet the Team
      # Choose which groups/teams of users to display.
      #   Edit `user_groups` in each user's profile to add them to one or more of these groups.
      user_groups:
          - Principal Investigator / Research Fellows / Staff
          - Graduate Students
          - Undergraduate Students
          - Visitors / Interns
          - Faculty Collaborators
      sort_by: Params.date
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: true

  - block: hero
    content:
      title: WING Alumni and Past Collaborators
      caption: "WING with alumni @ ACL '24 (Bangkok, Thailand)"
    design:
      background:
        image: 
          filename: 'acl24-banner.jpg'
          position: center
          size: cover             # Covers entire background
          filters:
            brightness: 0.2
        text_color_light: true
      parallax: true         # Optional parallax effect

  # Alumni Block
  - block: people
    content:
      user_groups:
          - Staff Alumni
          - Graduate Alumni
          - Undergraduate / Intern Alumni
          - Secondary School Alumni
          - Past Collaborators
      sort_by: Params.date
      sort_ascending: false
    design:
      show_interests: false
      show_role: true
      show_social: false
      show_avatar: false # this directive doesn't work  

---
