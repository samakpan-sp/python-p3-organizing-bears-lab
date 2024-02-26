select_all_female_bears_return_name_and_age = """
   SELECT bear.name, bear.age FROM bear WHERE sex = 'F';
"""


select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT * FROM bear ORDER BY name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
   SELECT bear.name, bear.age FROM bear WHERE alive = 'TRUE' ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT bear.name, bear.age FROM bear ORDER BY age DESC LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
   SELECT bear.name, bear.age FROM bear ORDER BY age ASC LIMIT 1;
"""


