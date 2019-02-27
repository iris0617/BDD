Feature:login


  @login
  Scenario: success
    Given go to login page
      When login with iris sylby071452
        Then redirect to dashboard page


    @login
  Scenario Outline: failed
    Given go to login page again
      When incorrect login with <username> and <password> again
        Then display error <message>
      Examples:data
      | username     | password   | message
      | iris         | incorrect  | Error:Wrong password
      | empty        | sylby071452 | Error:Username is empty
      | iris         | empty       | Error:Password is empty


    
