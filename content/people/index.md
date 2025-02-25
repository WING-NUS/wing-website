---
title: People
# date: 2022-10-24

type: landing

sections:
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
      sort_by: Params.date
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true

  - block: people
    content:
      user_groups:
          - Staff Alumni
          - Graduate Alumni
          - Undergraduate / Intern Alumni
          - Secondary School Alumni
      sort_by: Params.date
      sort_ascending: false
      design:
        show_interests: false
        show_role: true
        show_social: true
---
Test text for People.