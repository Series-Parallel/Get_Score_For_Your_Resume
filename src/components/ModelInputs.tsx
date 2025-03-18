import { Textarea } from "@heroui/react";
import { useFormik } from "formik";
import { useState } from "react";

export default function ModelInputs() {
  const [score, setScore] = useState<number | null>(null);

  const handleSubmit = async () => {
    console.log("Form Submitted", formik.values);

    const formData = new FormData();
    formData.append("jobDescription", formik.values.jobDescription);
    if (formik.values.resume) {
      formData.append("resume", formik.values.resume);
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/api/compare-resume", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setScore(data.score);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const formik = useFormik({
    enableReinitialize: false,
    initialValues: {
      jobDescription: "",
      resume: null as File | null,
    },
    onSubmit: handleSubmit,
  });
  console.log("Form values", formik.values);

  return (
    <form className="w-full flex flex-col items-center mt-[100px] mb-[20px] gap-4">
      {/* Job Description Textarea */}
      <Textarea
        name="jobDescription"
        label="Job Description"
        labelPlacement="outside"
        placeholder="Enter your description"
        variant="underlined"
        className="w-[500px]"
        value={formik.values.jobDescription}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
      {formik.touched.jobDescription && (
        <p className=" ml-[10px] text-red-400  text-[10px] h-[14px]">
          {formik.errors.jobDescription}
        </p>
      )}

      {/* File Input for Resume */}
      <div className="flex flex-col items-center">
        <input
          type="file"
          accept=".pdf"
          id="resume-upload"
          className="hidden"
          onChange={(event) => {
            const file = event.currentTarget.files?.[0] || null;
            formik.setFieldValue("resume", file);
          }}
        />
        <label
          htmlFor="resume-upload"
          className="px-6 py-2 bg-blue-600 text-white rounded-md cursor-pointer hover:bg-blue-700"
        >
          Upload Resume (PDF)
        </label>
        {formik.values.resume && (
          <p className="text-sm text-gray-700 mt-2">
            {formik.values.resume
              ? `Selected: ${formik.values.resume.name}`
              : "No file selected"}
          </p>
        )}
      </div>

      {/* Submit Button */}
      <button
        type="submit"
        disabled={formik.isSubmitting}
        className="px-6 py-2 bg-green-600 text-white rounded-md cursor-pointer hover:bg-green-700"
      >
        Submit
      </button>
      {score !== null && <p className="mt-4 text-lg">Match Score: {score}</p>}
    </form>
  );
}
