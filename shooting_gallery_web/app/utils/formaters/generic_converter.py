class GenericConverter:
    @staticmethod
    def convert_generic(new_value, reference_value, use_numpy: bool = False):
        if use_numpy:
            if len(new_value) == len(reference_value):
                return reference_value
            else:
                return new_value

        if new_value == reference_value:
            return reference_value

        if len(new_value) > 0 and new_value:
            reference_value = new_value

        return reference_value