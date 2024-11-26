# EPAIAssignment20
This assignment is all about class properties

### **Part 1: Properties and Property Decorators**  
Create a `Person` class with the following features:
1. **Dynamic Age Property**:  
   - Implement an `age` property. The age should not be stored directly but should be calculated based on the birth year and the current year using a dynamic property.
   - Provide a `set_birth_year` setter that allows modifying the birth year and updates the `age` accordingly.
   
2. **Full Name Property**:  
   - Implement a property `full_name` that combines `first_name` and `last_name`.
   - Add a setter for `full_name` that splits a full name string into `first_name` and `last_name` and updates both attributes.
   
3. **Computed Property with Validation**:  
   - Implement a `salary` property that computes the salary based on `base_salary` and an annual bonus percentage (given as a property `bonus`).
   - The salary should update automatically when either `base_salary` or `bonus` changes.
   - Add validation that the bonus percentage is between 0 and 100.

4. **Read-only Property for Current Year**:  
   - Implement a `current_year` property that returns the current year and is read-only.

### **Part 2: Read-Only and Computed Properties**  
1. **Circle Class**:  
   - Implement a `Circle` class with properties for `radius` and `diameter` (calculated property).
   - The `diameter` property should be computed as `2 * radius`, but the `radius` itself should be mutable.
   - Add a `set_radius` setter that recalculates the `diameter` and `area` whenever the radius is updated.
   
2. **Circle Area (Cached)**:  
   - Implement the `area` of the circle as a computed property.
   - Cache the computed area to avoid recalculating it every time the `area` property is accessed.
   
3. **Validation in Computed Properties**:  
   - Ensure that the `radius` is always a positive number. If it's set to a negative value, raise a `ValueError`.

### **Part 3: Class and Static Methods with Complex Use Cases**  
1. **Vehicle Class**:  
   - Create a `Vehicle` class with a class-level variable `vehicle_count` that tracks the total number of `Vehicle` instances.
   - Implement a class method `get_vehicle_count` that returns the current count.
   
2. **Static Method for Vehicle Classification**:  
   - Add a static method `classify_vehicle` that takes a string (`"car"`, `"truck"`, `"motorcycle"`) and returns a message like: `"This is a car"` or `"This is a truck"`.
   - This static method should not require any class or instance-specific data.

3. **Inheritance and Static Methods**:  
   - Create a subclass `ElectricVehicle` that inherits from `Vehicle`.
   - Override the `classify_vehicle` method to reflect that the vehicle is electric.

### **Part 4: Class Body Scope and Dynamic Behavior**  
1. **Advanced Class Body Scope**:  
   - Create a `DynamicClass` class with a class-level variable `static_value`.
   - Define an `__init__` method that allows the dynamic creation of attributes.
   - Implement a method `dynamic_attr` that dynamically adds attributes to an instance at runtime.
   
2. **Descriptor Protocol**:  
   - Implement a `ValidatedAttribute` descriptor that validates the value before setting it.
   - The `ValidatedAttribute` descriptor should ensure that any attribute set to this descriptor is always a positive integer.


