## Example with Ollama

1. Curl request

```
curl -X 'POST' \
  'http://0.0.0.0:8888/llm/generate?prompt=Between%20Lebron%20and%20Stepen%20Curry%2Cwho%20is%20taller.%20and%20how%20old%20are%20they' \
  -H 'accept: application/json' \
  -d ''
```

Output:

{"model":"llama3.1:8b","created_at":"2024-09-06T08:10:45.503840825Z","response":"A great question about two of the NBA's greatest players!\n\n**Height:**\nStephen Curry (also known as \"Steph\") is 6 feet tall, while LeBron James stands at an impressive **6'8\"**(198 cm).\n\n**Age:**\nAs of March 2023:\n\n* Stephen Curry is born on June 14, 1987 (age **35**)\n* LeBron James was born on December 30, 1984 (age **38**)","done":true,"done_reason":"stop","context":[128009,128006,882,128007,271,26556,2009,68557,323,3441,2821,47075,11,14965,374,51009,13,323,1268,2362,527,814,128009,128006,78191,128007,271,32,2294,3488,922,1403,315,279,17846,596,12474,4311,2268,334,3724,25,1035,54924,47075,320,19171,3967,439,330,8468,71,909,374,220,21,7693,16615,11,1418,58335,7957,13656,520,459,16358,3146,21,6,23,1,84825,3753,10166,3677,334,17166,25,1035,2170,315,5587,220,2366,18,1473,9,18587,47075,374,9405,389,5651,220,975,11,220,3753,22,320,425,3146,1758,334,340,9,58335,7957,574,9405,389,6790,220,966,11,220,3753,19,320,425,3146,1987,43042],"total_duration":66928834802,"load_duration":29026866,"prompt_eval_count":28,"prompt_eval_duration":284704000,"eval_count":97,"eval_duration":66613922000}
