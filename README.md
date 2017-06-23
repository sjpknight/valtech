Automation framework is MVP for the purposes of this test. I used the OO Language Python to script the entire test in a single file with assertions for each step. Clearly, in a production environment this would not scale and additional effort would be required to e.g. incorporate the Page Object or Screenplay patterns, and make the tests more atomic and resilient. However, for the purposes of this exercise, I felt the solution was sufficient as it covered all the required validations with minimal effort and code footprint.

I chose X-Path as the element selection mechanism for much the same reason. Although it is often deemed best practice to use CSS Selectors instead, for the sake of expediency I went with the quickest route to success. X-Path also has the benefit of highlighting whether elements have moved on the page, which in some regression test scenarios - can be useful.

The script can be executed using Python3. 

$ Python3 valtechTest.py
