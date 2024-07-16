#!/usr/bin/env python
# coding: utf-8

# In[3]:


def partially_synchronized_product(event_structure1, event_structure2):
    # Step 1: Synchronize common events
    common_events = set(event_structure1).intersection(event_structure2)
    synchronized_product = list(common_events)

    # Step 2: Extend with unique events from each structure
    for event in event_structure1:
        if event not in common_events:
            synchronized_product.append(event)
    for event in event_structure2:
        if event not in common_events:
            synchronized_product.append(event)

   

    return synchronized_product

#event structures
event_structure1a = [(0, 'Task1'), (1, 'OR'), (2, 'Task2'), (3, 'Task4'), (4,'Task5')]
event_structure1b = [(0, 'Task1'), (1, 'OR'), (2, 'Task3')]

event_structure2a = [(0, 'Task1'), (1, 'XOR'), (2, 'Task2'), (3, 'Task4')]
event_structure2b = [(0, 'Task1'), (1, 'XOR'), (2, 'Task3')]


# Compute the partially synchronized product
product1 = partially_synchronized_product(event_structure1a, event_structure2a)
product2 = partially_synchronized_product(event_structure1b, event_structure2b)
print("Partially Synchronized Product1:", product1)
print("Partially Synchronized Product2:", product2)


# In[4]:


def calculate_behavioral_similarity(event_structure1, event_structure2, synchronized_product):
    
    similarity1 = len(set(synchronized_product).intersection(event_structure1)) / len(set(synchronized_product).union(event_structure1))
    similarity2 = len(set(synchronized_product).intersection(event_structure2)) / len(set(synchronized_product).union(event_structure2))

    # Calculate the average similarity
    average_similarity = (similarity1 + similarity2) / 2
    return average_similarity

# Example event structures
event_structure1a = [(0, 'Task1'), (1, 'OR'), (2, 'Task2'), (3, 'Task4'), (4,'Task5')]
event_structure1b = [(0, 'Task1'), (1, 'OR'), (2, 'Task3')]

event_structure2a = [(0, 'Task1'), (1, 'XOR'), (2, 'Task2'), (3, 'Task4')]
event_structure2b = [(0, 'Task1'), (1, 'XOR'), (2, 'Task3')]



# Calculate behavioral similarity based on the partially synchronized product
behavioral_similarity1 = calculate_behavioral_similarity(event_structure1a, event_structure2a, product1)
print("Behavioral Similarity1:", behavioral_similarity1)

behavioral_similarity2 = calculate_behavioral_similarity(event_structure1b, event_structure2b, product2)
print("Behavioral Similarity2:", behavioral_similarity2)


# In[5]:


final_behavioral_similarity = (behavioral_similarity1 + behavioral_similarity2) / 2
print("Final Behavioral Similarity:", final_behavioral_similarity)


# In[ ]:




